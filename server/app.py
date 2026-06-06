# -*- coding: utf-8 -*-
"""
Flask 数据分享服务器
"""

import sys
import os
# 确保项目根目录在 Python 路径中
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import random
import string

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

from server.database import init_db, insert_share, get_share, delete_expired
from server.cleanup import start_cleanup, stop_cleanup

app = Flask(__name__)
CORS(app)


def _gen_code(length=6):
    """生成随机分享暗号（大写字母+数字）"""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))


@app.route('/api/share', methods=['POST'])
def upload():
    """上传热搜数据，返回暗号"""
    body = request.get_json(force=True)
    platform = body.get('platform', '')
    data = body.get('data', [])

    if not platform or not data:
        return jsonify({'error': 'platform 和 data 不能为空'}), 400

    code = _gen_code()
    # 确保暗号唯一（简单重试）
    for _ in range(5):
        if get_share(code) is None:
            break
        code = _gen_code()

    data_json = json.dumps(data, ensure_ascii=False)
    expires_at = insert_share(code, platform, data_json, expire_hours=1)

    return jsonify({
        'code': code,
        'expires_at': expires_at,
    })


@app.route('/api/share/<code>', methods=['GET'])
def download(code):
    """根据暗号获取数据"""
    result = get_share(code.upper())

    if result is None:
        return jsonify({'error': '暗号不存在，请检查输入是否正确'}), 404

    if result == 'expired':
        return jsonify({'error': '分享已过期（有效期1小时）'}), 410

    data = json.loads(result['data'])
    return jsonify({
        'platform': result['platform'],
        'data': data,
        'created_at': result['created_at'],
        'expires_at': result['expires_at'],
    })


@app.route('/view/<code>')
def view_page(code):
    """数据展示网页（接收方扫码打开）"""
    result = get_share(code.upper())

    if result is None:
        return _render_page('404', {'message': '暗号不存在，请检查输入是否正确'})
    if result == 'expired':
        return _render_page('expired', {'message': '分享已过期（有效期 1 小时）'})

    data = json.loads(result['data'])
    platform = result['platform']

    rows_html = ''
    for item in data:
        rank = item.get('rank', '')
        title = item.get('title', '')
        heat = item.get('heat', '')
        rows_html += f'<tr><td>{rank}</td><td class="title">{title}</td><td>{heat}</td></tr>'

    return _render_page('ok', {
        'platform': platform,
        'rows': rows_html,
        'count': len(data),
        'expires_at': result['expires_at'],
    })


def _render_page(status, ctx):
    """渲染展示页面"""
    if status == 'ok':
        body = f'''
        <div class="header">
            <h1>🔥 {ctx['platform']}热搜</h1>
            <p class="sub">共 {ctx['count']} 条 · 有效期至 {ctx['expires_at']}</p>
        </div>
        <table>
            <thead><tr><th>#</th><th>标题</th><th>热度</th></tr></thead>
            <tbody>{ctx['rows']}</tbody>
        </table>
        <p class="footer">数据来自share_tool工具</p>
        '''
    else:
        icon = '🔍' if status == '404' else '⏰'
        body = f'''
        <div class="error-box">
            <div class="icon">{icon}</div>
            <h2>{ctx['message']}</h2>
            <p>请向分享者索取新的暗号</p>
        </div>
        '''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>share_tool工具</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:"PingFang SC","Microsoft YaHei","Helvetica Neue",sans-serif;
       background:linear-gradient(180deg,#FFF0F3 0%,#FFF 100%); min-height:100vh;
       padding:24px 16px 48px; color:#333; }}
.header {{ text-align:center; padding:24px 0 16px; }}
.header h1 {{ font-size:22px; color:#C85568; }}
.header .sub {{ font-size:13px; color:#999; margin-top:6px; }}
table {{ width:100%; max-width:500px; margin:0 auto; border-collapse:collapse;
        background:#FFF; border-radius:12px; overflow:hidden;
        box-shadow:0 2px 12px rgba(232,104,122,0.1); }}
thead {{ background:#E0687A; }}
thead th {{ color:#FFF; font-size:14px; padding:12px 8px; text-align:center; font-weight:600; }}
thead th:first-child {{ width:36px; }}
thead th:last-child {{ width:80px; }}
tbody td {{ padding:11px 8px; font-size:14px; text-align:center;
            border-bottom:1px solid #FFF0F3; }}
tbody td.title {{ text-align:left; line-height:1.4; }}
tbody tr:nth-child(even) {{ background:#FFF0F3; }}
tbody tr:last-child td {{ border-bottom:none; }}
.error-box {{ text-align:center; padding:80px 24px; }}
.error-box .icon {{ font-size:64px; margin-bottom:16px; }}
.error-box h2 {{ font-size:18px; color:#C85568; margin-bottom:8px; }}
.error-box p {{ font-size:14px; color:#999; }}
.footer {{ text-align:center; font-size:12px; color:#CCC; padding:24px 0; }}
</style>
</head>
<body>{body}</body>
</html>'''
    return render_template_string(html)


@app.route('/api/health', methods=['GET'])
def health():
    """健康检查"""
    return jsonify({'status': 'ok'})


def run_server(port=5000):
    """启动服务器"""
    init_db()
    start_cleanup()
    try:
        app.run(host='0.0.0.0', port=port, debug=False)
    finally:
        stop_cleanup()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    print(f'数据分享服务器启动: http://0.0.0.0:{port}')
    run_server(port)
