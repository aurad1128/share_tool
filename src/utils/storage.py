# -*- coding: utf-8 -*-
"""
本地存储管理
"""

import os
import json


def get_save_dir():
    """获取/创建保存目录"""
    base = os.path.join(os.path.expanduser('~'), 'Documents', '面对面热搜爬虫工具')
    os.makedirs(base, exist_ok=True)
    return base


def get_history_path():
    return os.path.join(get_save_dir(), 'history.json')


def load_history():
    """加载历史记录"""
    path = get_history_path()
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []
    return []


def add_history(entry):
    """添加一条历史记录"""
    history = load_history()
    history.insert(0, entry)
    # 只保留最近 50 条
    if len(history) > 50:
        history = history[:50]
    with open(get_history_path(), 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
