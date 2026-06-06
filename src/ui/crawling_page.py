# -*- coding: utf-8 -*-
"""
爬取进度页 - 显示加载动画和状态
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer


class CrawlingPage(QWidget):
    """爬取进度页"""

    def __init__(self):
        super().__init__()
        self._dots = 0
        self._timer = QTimer()
        self._timer.timeout.connect(self._update_dots)
        self._platform = ''
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # 大号加载图标
        self.icon_label = QLabel('⏳')
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.icon_label.setStyleSheet('font-size: 80px;')
        layout.addWidget(self.icon_label)

        layout.addSpacing(24)

        # 状态文字
        self.status_label = QLabel('正在爬取数据...')
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet('color: #333333; font-size: 18px;')
        layout.addWidget(self.status_label)

        layout.addSpacing(8)

        # 提示文字
        self.hint_label = QLabel('请稍候片刻')
        self.hint_label.setAlignment(Qt.AlignCenter)
        self.hint_label.setStyleSheet('color: #666666; font-size: 14px;')
        layout.addWidget(self.hint_label)

        layout.addStretch()
        self.setLayout(layout)

    def set_platform(self, name):
        """设置当前爬取的平台名称"""
        self._platform = name
        self.status_label.setText(f'正在爬取{name}热搜...')

    def start_animation(self):
        """开始动画"""
        self._timer.start(500)

    def stop_animation(self):
        """停止动画"""
        self._timer.stop()
        self.icon_label.setText('✅')
        self.hint_label.setText('爬取完成！')

    def _update_dots(self):
        self._dots = (self._dots + 1) % 4
        self.icon_label.setText(f'⏳ 加载中{"." * self._dots}')
