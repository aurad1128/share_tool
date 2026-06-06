# -*- coding: utf-8 -*-
"""
客户端分享服务 — 上传/获取数据
"""

import time
import socket
import requests


SERVER_PORT = 5000
SERVER_URL = f'http://127.0.0.1:{SERVER_PORT}'
_lan_ip = ''
_public_url = ''


def set_public_url(url):
    """设置 ngrok 公网地址"""
    global _public_url
    _public_url = url.rstrip('/') if url else ''


def _detect_lan_ip():
    """探测本机局域网 IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('114.114.114.114', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'


def set_server_url(url):
    """修改服务器地址"""
    global SERVER_URL
    SERVER_URL = url.rstrip('/')


def upload_data(platform, data, retries=3):
    """上传热搜数据，返回 (code, expires_at)"""
    last_error = None
    for attempt in range(retries):
        try:
            resp = requests.post(
                f'{SERVER_URL}/api/share',
                json={'platform': platform, 'data': data},
                timeout=10,
            )
            resp.raise_for_status()
            result = resp.json()
            if 'error' in result:
                raise RuntimeError(result['error'])
            return result['code'], result['expires_at']
        except requests.ConnectionError as e:
            last_error = e
            if attempt < retries - 1:
                time.sleep(1)
        except Exception as e:
            raise e
    raise RuntimeError(f'无法连接到分享服务器，请稍后重试\n{last_error}')


def get_share_url(code):
    """生成分享链接（优先用 ngrok 公网地址，其次局域网 IP）"""
    global _lan_ip, _public_url
    if _public_url:
        return f'{_public_url}/view/{code}'
    if not _lan_ip:
        _lan_ip = _detect_lan_ip()
    return f'http://{_lan_ip}:{SERVER_PORT}/view/{code}'


def fetch_data(code):
    """根据暗号获取数据，返回 dict 或 None（过期）"""
    resp = requests.get(
        f'{SERVER_URL}/api/share/{code}',
        timeout=10,
    )
    if resp.status_code == 404:
        raise RuntimeError('暗号不存在')
    if resp.status_code == 410:
        return None  # 过期
    resp.raise_for_status()
    result = resp.json()
    if 'error' in result:
        raise RuntimeError(result['error'])
    return result
