# -*- coding: utf-8 -*-
"""
爬虫基类
"""

import requests


class BaseCrawler:
    """所有爬虫的基类"""

    platform_name = ''

    HEADERS = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/125.0.0.0 Safari/537.36'
        ),
        'Accept': (
            'text/html,application/xhtml+xml,application/xml;q=0.9,'
            'image/webp,*/*;q=0.8'
        ),
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
    }

    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(self.HEADERS)
        self._timeout = 10

    def crawl(self):
        """子类必须实现此方法"""
        raise NotImplementedError

    def _get(self, url, **kwargs):
        kwargs.setdefault('timeout', self._timeout)
        return self._session.get(url, **kwargs)

    def _format_result(self, items):
        """将原始数据统一格式化"""
        results = []
        for i, item in enumerate(items[:10]):
            results.append({
                'rank': i + 1,
                'title': item.get('title', ''),
                'heat': item.get('heat', ''),
            })
        return results
