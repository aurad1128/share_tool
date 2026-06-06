# -*- coding: utf-8 -*-
"""
结果展示页 - 数据表格、二维码（带滚动区域）
"""

from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,
    QScrollArea, QFrame
)
from utils.qr_generator import generate_qr
from utils.share_service import get_share_url


class ResultPage(QScrollArea):
    """结果展示页（可滚动）"""

    back_clicked = pyqtSignal()
    save_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._remaining = 3600
        self._timer = QTimer()
        self._timer.timeout.connect(self._tick)

        self.setWidgetResizable(True)
        self.setFrameShape(QFrame.NoFrame)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._content = QWidget()
        self.setWidget(self._content)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self._content)
        layout.setContentsMargins(40, 32, 40, 32)
        layout.setSpacing(28)

        # ── 成功提示 ──
        self.success_label = QLabel('✅ 爬取成功')
        self.success_label.setAlignment(Qt.AlignCenter)
        self.success_label.setStyleSheet(
            'color: #C85568; font-size: 20px; font-weight: bold;'
        )
        layout.addWidget(self.success_label)

        # ── 表格卡片 ──
        card = QFrame()
        card.setStyleSheet(
            'QFrame {'
            'background-color: #FFF0F3;'
            'border-radius: 14px;'
            'border: 1px solid #F0B0B8;'
            '}'
        )
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(0, 0, 0, 0)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['排名', '标题', '热度值'])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.table.horizontalHeader().resizeSection(0, 60)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.table.horizontalHeader().resizeSection(2, 100)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setMinimumHeight(260)
        self.table.setMaximumHeight(420)
        self.table.setShowGrid(False)
        card_layout.addWidget(self.table)

        layout.addWidget(card)

        # ── 二维码 ──
        qr_title = QLabel('📱 扫一扫分享给朋友')
        qr_title.setAlignment(Qt.AlignCenter)
        qr_title.setStyleSheet('font-size: 16px; color: #666666; font-weight: bold;')
        layout.addWidget(qr_title)

        self.qr_label = QLabel()
        self.qr_label.setFixedSize(180, 180)
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.qr_label.setStyleSheet(
            'border: 2px solid #F0B0B8; border-radius: 12px;'
            'background-color: #FFF0F3;'
        )
        self.qr_label.setText('生成中...')

        qr_row = QHBoxLayout()
        qr_row.addStretch()
        qr_row.addWidget(self.qr_label)
        qr_row.addStretch()
        layout.addLayout(qr_row)

        # ── 有效期 ──
        self.expire_label = QLabel()
        self.expire_label.setAlignment(Qt.AlignCenter)
        self.expire_label.setStyleSheet('color: #999999; font-size: 14px;')
        self._update_expire_text()
        layout.addWidget(self.expire_label)

        # ── 底部按钮 ──
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        save_btn = QPushButton('💾 保存 Excel')
        save_btn.setMinimumSize(160, 46)
        save_btn.setCursor(Qt.PointingHandCursor)
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #E0687A; color: white;
                border: none; border-radius: 8px;
                font-size: 15px; font-weight: bold; padding: 8px 24px;
            }
            QPushButton:hover { background-color: #F0909B; }
            QPushButton:pressed { background-color: #C85568; }
        """)
        save_btn.clicked.connect(self.save_clicked.emit)
        btn_layout.addWidget(save_btn)

        btn_layout.addSpacing(16)

        back_btn = QPushButton('← 返回功能列表')
        back_btn.setMinimumSize(160, 46)
        back_btn.setCursor(Qt.PointingHandCursor)
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: white; color: #E0687A;
                border: 2px solid #E0687A; border-radius: 8px;
                font-size: 15px; font-weight: bold; padding: 8px 24px;
            }
            QPushButton:hover { background-color: #FFF0F3; }
        """)
        back_btn.clicked.connect(self.back_clicked.emit)
        btn_layout.addWidget(back_btn)

        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        layout.addStretch()

    def set_data(self, platform, records):
        self.table.setRowCount(len(records))
        for i, rec in enumerate(records):
            self.table.setItem(i, 0, self._cell(rec.get('rank', '')))
            self.table.setItem(i, 1, self._cell(rec.get('title', '')))
            self.table.setItem(i, 2, self._cell(rec.get('heat', '')))
        self.success_label.setText(f'✅ {platform}热搜爬取成功')

    def set_share_info(self, code):
        try:
            url = get_share_url(code)
            pixmap = generate_qr(url, size=170)
            self.qr_label.setPixmap(pixmap)
            self.qr_label.setStyleSheet('border: none; background: transparent;')
        except Exception:
            self.qr_label.setText('生成失败')

    def start_countdown(self):
        self._remaining = 3600
        self._timer.start(1000)

    def stop_countdown(self):
        self._timer.stop()

    def _tick(self):
        self._remaining -= 1
        if self._remaining <= 0:
            self._timer.stop()
            self.expire_label.setText('⏰ 分享已过期')
            return
        self._update_expire_text()

    def _update_expire_text(self):
        m, s = divmod(self._remaining, 60)
        self.expire_label.setText(f'有效期剩余 {m} 分 {s:02d} 秒')

    def _cell(self, text):
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(Qt.AlignCenter)
        return item
