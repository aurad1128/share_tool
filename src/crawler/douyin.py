# -*- coding: utf-8 -*-
"""
抖音热搜爬虫
"""

from crawler.base import BaseCrawler


class DouyinCrawler(BaseCrawler):
    platform_name = '抖音'

    # 免费聚合 API（来源排序按可靠性）
    API_URLS = [
        'https://api.xunjinlu.fun/api/rebang/douyin.php',
        'https://60s.viki.moe/v2/douyin',
        'https://apis.lolimi.cn/api/hot/douyin',
    ]

    def __init__(self):
        super().__init__()
        self._session.headers['Referer'] = 'https://www.douyin.com/'

    def crawl(self):
        errors = []
        for url in self.API_URLS:
            try:
                return self._try_api(url)
            except Exception as e:
                errors.append(str(e))
                continue

        raise RuntimeError(
            '抖音热搜爬取失败\n\n'
            '所有备用接口均返回失败，请检查网络后重试。\n'
            '或尝试使用微博/B站热搜。'
        )

    def _try_api(self, url):
        resp = self._get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        # 不同 API 的返回格式处理
        items = None

        if 'data' in data:
            d = data['data']
            if isinstance(d, list):
                items = d
            elif isinstance(d, dict):
                items = d.get('list') or d.get('data') or d.get('items') or []

        if not items and 'list' in data:
            items = data['list']

        if not items and 'result' in data:
            items = data['result']

        if not items:
            raise RuntimeError('返回数据为空或格式不识别')

        results = []
        for i, item in enumerate(items[:10]):
            title = (
                item.get('name') or item.get('word') or
                item.get('title') or item.get('keyword') or ''
            )
            hot = (
                item.get('hot') or item.get('hot_value') or
                item.get('hotValue') or item.get('heat') or ''
            )
            heat_str = f'{hot:,}' if isinstance(hot, int) else str(hot) if hot else ''
            results.append({'rank': i + 1, 'title': title, 'heat': heat_str})

        return results
