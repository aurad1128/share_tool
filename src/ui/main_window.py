# -*- coding: utf-8 -*-
"""
主窗口 - 管理所有页面和切换逻辑
"""

import sys
import os
import logging
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

from config import WINDOW_CONFIG, APP_NAME, APP_VERSION
from ui.home_page import HomePage
from ui.function_list_page import FunctionListPage
from ui.crawling_page import CrawlingPage
from ui.result_page import ResultPage
from crawler.weibo import WeiboCrawler
from crawler.bilibili import BilibiliCrawler
from crawler.douyin import DouyinCrawler
from utils.excel_handler import save_to_excel
from utils.share_service import upload_data

# 日志配置
log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..')
logging.basicConfig(
    filename=os.path.join(log_dir, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    encoding='utf-8',
)
logging.info('=== 应用启动 ===')


def _friendly_error(msg):
    """把技术错误翻译成用户能懂的话"""
    lower = msg.lower()
    if 'connection' in lower or 'connect' in lower or 'timeout' in lower:
        return '网络连接失败，请检查网络后重试'
    if '403' in msg or 'forbidden' in msg:
        return '网站拒绝了访问，Cookie 可能已过期'
    if '404' in msg:
        return '数据接口不存在，网站可能改版了'
    if 'cookie' in lower:
        return '登录信息已过期，请更新 Cookie'
    if 'ssl' in lower or 'certificate' in lower:
        return '网络连接不安全，请检查系统时间或网络环境'
    if len(msg) > 80:
        return msg[:80] + '...'
    return msg


class ServerThread(QThread):
    """后台 Flask 服务器（线程内直跑，兼容打包与开发）"""

    def run(self):
        from server.app import init_db, start_cleanup, app
        init_db()
        start_cleanup()
        try:
            app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
        except Exception:
            pass


class CrawlWorker(QThread):
    """后台爬虫"""
    finished = pyqtSignal(list)
    error = pyqtSignal(str)

    def __init__(self, crawler):
        super().__init__()
        self._crawler = crawler

    def run(self):
        try:
            data = self._crawler.crawl()
            self.finished.emit(data)
        except Exception as e:
            logging.error(f'Crawl error: {e}')
            self.error.emit(str(e))


class UploadWorker(QThread):
    """后台上传"""
    finished = pyqtSignal(str, str)
    error = pyqtSignal(str)

    def __init__(self, platform, data):
        super().__init__()
        self._platform = platform
        self._data = data

    def run(self):
        try:
            code, expires_at = upload_data(self._platform, self._data)
            self.finished.emit(code, expires_at)
        except Exception as e:
            logging.warning(f'Upload error: {e}')
            self.error.emit(str(e))


class MainWindow(QMainWindow):
    """主窗口"""

    CRAWLERS = {
        '微博': WeiboCrawler,
        'B站': BilibiliCrawler,
        '抖音': DouyinCrawler,
    }

    def __init__(self):
        super().__init__()
        self._worker = None
        self._upload_worker = None
        self._current_platform = ''
        self._crawl_data = []
        self._share_code = ''
        self._server_started = False
        self._crawling = False

        self.init_ui()
        self._connect_signals()

    def _ensure_server(self):
        if self._server_started:
            return
        self._server_started = True
        self._server_thread = ServerThread()
        self._server_thread.start()

    def init_ui(self):
        self.setWindowTitle(f'{APP_NAME} v{APP_VERSION}')
        self.resize(WINDOW_CONFIG['default_width'], WINDOW_CONFIG['default_height'])
        self.setMinimumSize(WINDOW_CONFIG['min_width'], WINDOW_CONFIG['min_height'])
        self._center_window()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_page = HomePage()
        self.function_list_page = FunctionListPage()
        self.crawling_page = CrawlingPage()
        self.result_page = ResultPage()

        for page in [self.home_page, self.function_list_page, self.crawling_page,
                     self.result_page]:
            self.stacked_widget.addWidget(page)

        self.stacked_widget.setCurrentWidget(self.home_page)

    def _connect_signals(self):
        self.home_page.start_clicked.connect(self._go_function_list)

        self.function_list_page.weibo_clicked.connect(lambda: self._go_crawling('微博'))
        self.function_list_page.bilibili_clicked.connect(lambda: self._go_crawling('B站'))
        self.function_list_page.douyin_clicked.connect(lambda: self._go_crawling('抖音'))
        self.result_page.back_clicked.connect(self._go_function_list)
        self.result_page.save_clicked.connect(self._save_excel)

    # ─── 页面跳转 ──────────────────────────────

    def _go_home(self):
        self.result_page.stop_countdown()
        self.stacked_widget.setCurrentWidget(self.home_page)

    def _go_function_list(self):
        self.result_page.stop_countdown()
        self.stacked_widget.setCurrentWidget(self.function_list_page)

    def _go_crawling(self, platform):
        if self._crawling:
            return  # 防止重复点击
        self._crawling = True
        self._ensure_server()
        self._current_platform = platform
        self._share_code = ''
        self.crawling_page.set_platform(platform)
        self.crawling_page.start_animation()
        self.stacked_widget.setCurrentWidget(self.crawling_page)

        crawler_cls = self.CRAWLERS.get(platform)
        if crawler_cls is None:
            self._on_crawl_error('未知平台')
            return

        self._worker = CrawlWorker(crawler_cls())
        self._worker.finished.connect(self._on_crawl_done)
        self._worker.error.connect(self._on_crawl_error)
        self._worker.start()

    def _on_crawl_done(self, data):
        self._crawling = False
        self._crawl_data = data
        self.crawling_page.stop_animation()

        self.result_page.set_data(self._current_platform, data)
        self.result_page.set_share_info('获取中...')
        self.result_page.start_countdown()
        self.stacked_widget.setCurrentWidget(self.result_page)

        self._upload_worker = UploadWorker(self._current_platform, data)
        self._upload_worker.finished.connect(self._on_upload_done)
        self._upload_worker.error.connect(self._on_upload_error)
        self._upload_worker.start()

    def _on_upload_done(self, code, expires_at):
        self._share_code = code
        self.result_page.set_share_info(code)

    def _on_upload_error(self, msg):
        import random
        import string
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        self._share_code = code
        self.result_page.set_share_info(code)
        # 上传失败只在后台日志记录，不弹窗打扰用户

    def _on_crawl_error(self, msg):
        self._crawling = False
        self.crawling_page.stop_animation()
        self.stacked_widget.setCurrentWidget(self.function_list_page)
        friendly = _friendly_error(msg)
        QMessageBox.warning(
            self, '爬取失败',
            f'{self._current_platform}热搜爬取失败\n\n{friendly}\n\n请检查网络后重试，或尝试其他平台。'
        )

    def _save_excel(self):
        if not self._crawl_data:
            QMessageBox.warning(self, '提示', '没有可保存的数据，请先爬取热搜。')
            return
        try:
            filepath = save_to_excel(self._crawl_data, self._current_platform)
            QMessageBox.information(
                self, '保存成功',
                f'文件已保存到：\n{filepath}\n\n文件夹已打开，可双击文件查看。'
            )
        except PermissionError:
            QMessageBox.warning(self, '保存失败',
                '没有权限写入文件，请检查文件夹权限或更换保存位置。')
        except OSError:
            QMessageBox.warning(self, '保存失败',
                '磁盘空间不足或文件被占用，请清理磁盘后重试。')
        except Exception as e:
            QMessageBox.warning(self, '保存失败',
                f'保存时出现问题，请重试。\n\n如果持续失败，请检查磁盘空间。')

    def _center_window(self):
        from PyQt5.QtWidgets import QApplication
        screen = QApplication.desktop().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2)
