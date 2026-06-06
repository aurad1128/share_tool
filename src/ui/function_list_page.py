# -*- coding: utf-8 -*-
"""
功能列表页 - 卡片式选择爬取平台
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont


PLATFORMS = [
    ('\U0001f4f1', '微博热搜', '实时热搜榜单 Top 10'),
    ('\U0001f4fa', 'B站热搜', '实时热搜榜单 Top 10'),
    ('\U0001f3b5', '抖音热搜', '实时热搜榜单 Top 10'),
]


class _ClickableCard(QFrame):
    """可点击卡片（带悬停效果）"""
    clicked = pyqtSignal()

    _NORMAL = 'QFrame { background-color:white; border:2px solid #F0B0B8; border-radius:14px; }'
    _HOVER = 'QFrame { background-color:#FFF0F3; border:2px solid #E0687A; border-radius:14px; }'

    def __init__(self):
        super().__init__()
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(self._NORMAL)

    def enterEvent(self, event):
        self.setStyleSheet(self._HOVER)

    def leaveEvent(self, event):
        self.setStyleSheet(self._NORMAL)

    def mousePressEvent(self, event):
        self.clicked.emit()


class FunctionListPage(QWidget):
    """功能列表页"""

    weibo_clicked = pyqtSignal()
    bilibili_clicked = pyqtSignal()
    douyin_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(48, 56, 48, 32)

        title = QLabel('选择爬取平台')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('color: #333333; font-size: 24px; font-weight: bold;')
        layout.addWidget(title)

        layout.addSpacing(36)

        items = [
            (PLATFORMS[0], self.weibo_clicked),
            (PLATFORMS[1], self.bilibili_clicked),
            (PLATFORMS[2], self.douyin_clicked),
        ]

        for (icon, name, desc), signal in items:
            card = self._make_card(icon, name, desc, signal)
            layout.addWidget(card)
            layout.addSpacing(20)

        layout.addStretch()
        self.setLayout(layout)

    def _make_card(self, icon, name, desc, signal):
        card = _ClickableCard()
        card.setMinimumHeight(90)
        card.clicked.connect(signal.emit)

        inner = QHBoxLayout(card)
        inner.setContentsMargins(24, 16, 24, 16)
        inner.setSpacing(20)

        icon_label = QLabel(icon)
        icon_label.setFixedWidth(50)
        icon_label.setStyleSheet('font-size: 32px; border: none; background: none;')
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        inner.addWidget(icon_label)

        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)

        name_label = QLabel(name)
        name_label.setFont(QFont('Microsoft YaHei', 17, QFont.Bold))
        name_label.setStyleSheet('color: #333333; border: none; background: none;')
        name_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        text_layout.addWidget(name_label)

        desc_label = QLabel(desc)
        desc_label.setFont(QFont('Microsoft YaHei', 12))
        desc_label.setStyleSheet('color: #999999; border: none; background: none;')
        desc_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        text_layout.addWidget(desc_label)

        inner.addLayout(text_layout)
        inner.addStretch()

        arrow = QLabel('›')
        arrow.setStyleSheet('font-size: 28px; color: #E0687A; border: none; background: none;')
        arrow.setAlignment(Qt.AlignCenter)
        arrow.setAttribute(Qt.WA_TransparentForMouseEvents)
        inner.addWidget(arrow)

        return card
