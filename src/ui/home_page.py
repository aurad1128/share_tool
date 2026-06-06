# -*- coding: utf-8 -*-
"""
主页 - 欢迎页面
"""

import os, sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QMovie


def _get_root():
    """项目根目录（兼容 PyInstaller 打包）"""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROJ_ROOT = _get_root()


class HomePage(QWidget):
    """主页组件"""

    start_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._movie = None
        self.init_ui()

    def init_ui(self):
        """初始化UI"""
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        layout.addStretch()

        # 动态小狗（粉色圆形容器居中）
        gif_path = os.path.join(PROJ_ROOT, 'cutedog.gif')

        container = QFrame()
        container.setFixedSize(240, 240)
        container.setStyleSheet(
            'background-color: #FFF0F3; border-radius: 120px; border: 3px solid #F0B0B8;'
        )

        dog_label = QLabel(container)
        dog_label.setAlignment(Qt.AlignCenter)
        dog_label.setFixedSize(200, 200)
        dog_label.move(20, 20)
        if os.path.exists(gif_path):
            self._movie = QMovie(gif_path)
            self._movie.setScaledSize(dog_label.size())
            dog_label.setMovie(self._movie)
            self._movie.start()

        # 居中容器
        row = QHBoxLayout()
        row.addStretch()
        row.addWidget(container)
        row.addStretch()
        layout.addLayout(row)

        layout.addSpacing(24)

        # 标语
        title = QLabel("欢迎使用面对面热搜爬虫工具")
        title.setStyleSheet("""
            QLabel {
                color: #C85568;
                font-size: 36px;
                font-weight: bold;
            }
        """)
        title.setAlignment(Qt.AlignCenter)
        
        # 副标题
        subtitle = QLabel("一键爬取热搜，轻松分享数据")
        subtitle.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 18px;
            }
        """)
        subtitle.setAlignment(Qt.AlignCenter)
        
        # 间距
        layout.addStretch()
        layout.addWidget(title)
        layout.addSpacing(16)
        layout.addWidget(subtitle)
        layout.addSpacing(48)
        
        # 开始按钮
        start_btn = QPushButton("开始使用")
        start_btn.setMinimumSize(200, 48)
        start_btn.setCursor(Qt.PointingHandCursor)
        start_btn.clicked.connect(self.on_start_clicked)
        
        # 按钮居中
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(start_btn)
        btn_layout.addStretch()
        
        layout.addLayout(btn_layout)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def on_start_clicked(self):
        """开始按钮点击事件"""
        self.start_clicked.emit()
