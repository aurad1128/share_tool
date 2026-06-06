# -*- coding: utf-8 -*-
"""
微博热搜爬虫
"""

from crawler.base import BaseCrawler
from crawler.cookies import WEIBO_COOKIES


class WeiboCrawler(BaseCrawler):
    platform_name = '微博'

    API_URL = 'https://weibo.com/ajax/side/hotSearch'

    def __init__(self):
        super().__init__()
        self._session.headers['Referer'] = 'https://weibo.com/'
        # 设置登录 Cookie
        for name, value in WEIBO_COOKIES.items():
            self._session.cookies.set(name, value, domain='.weibo.com')

    def crawl(self):
        resp = self._get(self.API_URL)
        resp.raise_for_status()
        data = resp.json()

        realtime = data.get('data', {}).get('realtime', [])
        if not realtime:
            raise RuntimeError('微博返回数据为空，Cookie 可能已过期，请更新 cookies.py')

        results = []
        for i, item in enumerate(realtime[:10]):
            raw_hot = item.get('raw_hot') or item.get('num') or 0
            heat_str = f'{raw_hot:,}' if isinstance(raw_hot, int) else str(raw_hot)
            results.append({
                'rank': i + 1,
                'title': item.get('word', ''),
                'heat': heat_str,
            })
        return results
