# -*- coding: utf-8 -*-
"""
定时清理过期数据
"""

from apscheduler.schedulers.background import BackgroundScheduler
from server.database import delete_expired


scheduler = BackgroundScheduler()


def start_cleanup():
    """启动定时清理任务（每10分钟执行一次）"""
    scheduler.add_job(
        delete_expired,
        'interval',
        minutes=10,
        id='cleanup',
        replace_existing=True,
    )
    scheduler.start()


def stop_cleanup():
    """停止定时清理"""
    if scheduler.running:
        scheduler.shutdown(wait=False)
