# -*- coding: utf-8 -*-
"""
B站热搜爬虫
"""

from crawler.base import BaseCrawler


class BilibiliCrawler(BaseCrawler):
    platform_name = 'B站'

    # 移动端接口，无需 WBI 签名
    MOBILE_URL = 'https://app.bilibili.com/x/v2/search/trending/ranking'
    # 旧版接口（备用1）
    OLD_URL = 'https://s.search.bilibili.com/main/hotword'
    # 免费聚合 API（备用2）
    FALLBACK_URL = 'https://tenapi.cn/v2/bilihot'

    def __init__(self):
        super().__init__()
        self._session.headers['Referer'] = 'https://m.bilibili.com/'

    def crawl(self):
        for method in [self._crawl_mobile, self._crawl_old, self._crawl_fallback]:
            try:
                return method()
            except Exception:
                continue

        raise RuntimeError(
            'B站热搜爬取失败\n\n'
            '请检查网络连接后重试，或尝试其他平台。'
        )

    def _crawl_mobile(self):
        resp = self._get(self.MOBILE_URL, params={'limit': 10})
        resp.raise_for_status()
        data = resp.json()
        if data.get('code') != 0:
            raise RuntimeError(f'code={data.get("code")}')
        items = data.get('data', {}).get('list', [])
        if not items:
            raise RuntimeError('返回数据为空')

        results = []
        for i, item in enumerate(items[:10]):
            title = item.get('show_name') or item.get('keyword', '')
            hot_id = item.get('hot_id', '')
            results.append({
                'rank': i + 1,
                'title': title,
                'heat': f'热度 {hot_id}' if hot_id else '',
            })
        return results

    def _crawl_old(self):
        resp = self._get(self.OLD_URL)
        resp.raise_for_status()
        data = resp.json()
        items = data.get('list', [])
        if not items:
            raise RuntimeError('返回数据为空')
        results = []
        for i, item in enumerate(items[:10]):
            results.append({
                'rank': i + 1,
                'title': item.get('show_name') or item.get('word', ''),
                'heat': '',
            })
        return results

    def _crawl_fallback(self):
        resp = self._get(self.FALLBACK_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data.get('code') != 200:
            raise RuntimeError(f'code={data.get("code")}')
        items = data.get('data', [])
        if not items:
            raise RuntimeError('返回数据为空')
        results = []
        for i, item in enumerate(items[:10]):
            results.append({
                'rank': i + 1,
                'title': item.get('name') or item.get('title', ''),
                'heat': str(item.get('hot') or ''),
            })
        return results
