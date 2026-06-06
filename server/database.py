# -*- coding: utf-8 -*-
"""
SQLite 数据库操作
"""

import os
import sqlite3
from datetime import datetime, timedelta


DB_PATH = os.path.join(os.path.dirname(__file__), 'shares.db')


def _connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """初始化数据库，创建表"""
    conn = _connect()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS shares (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            platform TEXT NOT NULL,
            data_json TEXT NOT NULL,
            created_at TEXT NOT NULL,
            expires_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def insert_share(code, platform, data_json, expire_hours=1):
    """插入一条分享记录"""
    now = datetime.now()
    expires = now + timedelta(hours=expire_hours)
    conn = _connect()
    conn.execute(
        'INSERT INTO shares (code, platform, data_json, created_at, expires_at) '
        'VALUES (?, ?, ?, ?, ?)',
        (code, platform, data_json,
         now.strftime('%Y-%m-%d %H:%M:%S'),
         expires.strftime('%Y-%m-%d %H:%M:%S'))
    )
    conn.commit()
    conn.close()
    return expires.strftime('%Y-%m-%d %H:%M:%S')


def get_share(code):
    """根据暗号获取分享数据，过期返回 None"""
    conn = _connect()
    row = conn.execute(
        'SELECT * FROM shares WHERE code = ?', (code,)
    ).fetchone()
    conn.close()

    if row is None:
        return None  # 不存在

    expires_at = datetime.strptime(row['expires_at'], '%Y-%m-%d %H:%M:%S')
    if datetime.now() > expires_at:
        return 'expired'

    return {
        'platform': row['platform'],
        'data': row['data_json'],
        'created_at': row['created_at'],
        'expires_at': row['expires_at'],
    }


def delete_expired():
    """删除所有过期记录，返回删除数量"""
    conn = _connect()
    cursor = conn.execute(
        "DELETE FROM shares WHERE datetime(expires_at) < datetime('now', 'localtime')"
    )
    count = cursor.rowcount
    conn.commit()
    conn.close()
    return count
