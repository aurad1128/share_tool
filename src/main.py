# -*- coding: utf-8 -*-
"""
主程序入口
"""

import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

# PyInstaller 兼容：确定根目录
if getattr(sys, 'frozen', False):
    _ROOT = sys._MEIPASS
else:
    _ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(_ROOT, 'src') if os.path.isdir(os.path.join(_ROOT, 'src')) else _ROOT)

from ui.main_window import MainWindow


def main():
    """主函数"""
    # 非打包模式才需要手动设 Qt 插件路径
    if not getattr(sys, 'frozen', False):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        qt_plugin_path = os.path.join(
            project_root, 'venv', 'Lib', 'site-packages', 'PyQt5', 'Qt5', 'plugins'
        )
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = qt_plugin_path

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    # 加载全局样式表
    style_path = os.path.join(_ROOT, 'src', 'resources', 'styles.qss')
    if os.path.exists(style_path):
        with open(style_path, 'r', encoding='utf-8') as f:
            app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
