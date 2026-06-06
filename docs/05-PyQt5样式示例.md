# PyQt5 样式示例代码

## 完整的QSS样式表

```python
# styles.py - 完整的应用样式表

MAIN_STYLESHEET = """
/* ========== 全局样式 ========== */
QMainWindow {
    background-color: #FFFFFF;
}

QWidget {
    font-family: 'Microsoft YaHei', '微软雅黑';
    font-size: 16px;
    color: #333333;
}

/* ========== 按钮样式 ========== */
QPushButton {
    background-color: #FFB6C1;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 32px;
    font-size: 16px;
    font-weight: bold;
    min-height: 40px;
}

QPushButton:hover {
    background-color: #FFD1DC;
}

QPushButton:pressed {
    background-color: #FF9EAF;
}

QPushButton:disabled {
    background-color: #CCCCCC;
    color: #999999;
}

/* 次要按钮 */
QPushButton#secondaryButton {
    background-color: white;
    color: #FFB6C1;
    border: 2px solid #FFB6C1;
}

QPushButton#secondaryButton:hover {
    background-color: #FFF0F5;
}

/* ========== 输入框样式 ========== */
QLineEdit {
    border: 2px solid #FFD1DC;
    border-radius: 4px;
    padding: 8px 16px;
    font-size: 16px;
    background-color: white;
    color: #333333;
}

QLineEdit:focus {
    border-color: #FFB6C1;
}

QLineEdit:disabled {
    background-color: #F5F5F5;
    color: #CCCCCC;
}

/* ========== 表格样式 ========== */
QTableWidget {
    border: 1px solid #FFD1DC;
    border-radius: 8px;
    background-color: white;
    gridline-color: #FFF0F5;
}

QTableWidget::item {
    padding: 8px;
    border-bottom: 1px solid #FFF0F5;
}

QTableWidget::item:selected {
    background-color: #FFF0F5;
    color: #333333;
}

QHeaderView::section {
    background-color: #FFF0F5;
    color: #333333;
    padding: 12px;
    border: none;
    border-bottom: 2px solid #FFD1DC;
    font-weight: bold;
}

/* ========== 标签样式 ========== */
QLabel {
    color: #333333;
    background-color: transparent;
}

QLabel#titleLabel {
    font-size: 48px;
    font-weight: bold;
    color: #FFB6C1;
}

QLabel#subtitleLabel {
    font-size: 24px;
    color: #666666;
}

/* ========== 滚动条样式 ========== */
QScrollBar:vertical {
    border: none;
    background-color: #FFF0F5;
    width: 10px;
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background-color: #FFD1DC;
    border-radius: 5px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #FFB6C1;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

/* ========== 消息框样式 ========== */
QMessageBox {
    background-color: white;
}

QMessageBox QPushButton {
    min-width: 80px;
}

/* ========== 进度条样式 ========== */
QProgressBar {
    border: 2px solid #FFD1DC;
    border-radius: 8px;
    text-align: center;
    background-color: white;
    color: #333333;
}

QProgressBar::chunk {
    background-color: #FFB6C1;
    border-radius: 6px;
}

/* ========== 工具提示样式 ========== */
QToolTip {
    background-color: #FFB6C1;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 8px;
    font-size: 14px;
}
"""
```

## 使用示例

### 1. 应用全局样式

```python
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("面对面传输工具")
        self.setGeometry(100, 100, 800, 600)
        
        # 应用样式表
        self.setStyleSheet(MAIN_STYLESHEET)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

### 2. 创建主页

```python
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(32)
        
        # 标语
        title = QLabel("欢迎使用面对面传输工具")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignCenter)
        
        # 开始按钮
        start_btn = QPushButton("开始使用")
        start_btn.setMinimumWidth(200)
        start_btn.setMinimumHeight(48)
        start_btn.clicked.connect(self.on_start_clicked)
        
        layout.addWidget(title)
        layout.addWidget(start_btn)
        
        self.setLayout(layout)
    
    def on_start_clicked(self):
        print("开始使用")
```

### 3. 创建功能列表页

```python
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class FunctionListPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(48, 32, 48, 32)
        layout.setSpacing(16)
        
        # 标题
        title = QLabel("选择要爬取的平台")
        title.setObjectName("subtitleLabel")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        layout.addSpacing(16)
        
        # 微博按钮
        weibo_btn = QPushButton("📱 微博热搜")
        weibo_btn.setMinimumHeight(80)
        weibo_btn.clicked.connect(lambda: self.on_crawler_clicked("weibo"))
        layout.addWidget(weibo_btn)
        
        # B站按钮
        bilibili_btn = QPushButton("📺 B站热搜")
        bilibili_btn.setMinimumHeight(80)
        bilibili_btn.clicked.connect(lambda: self.on_crawler_clicked("bilibili"))
        layout.addWidget(bilibili_btn)
        
        # 抖音按钮
        douyin_btn = QPushButton("🎵 抖音热搜")
        douyin_btn.setMinimumHeight(80)
        douyin_btn.clicked.connect(lambda: self.on_crawler_clicked("douyin"))
        layout.addWidget(douyin_btn)
        
        layout.addSpacing(16)
        
        # 接收数据按钮
        receive_btn = QPushButton("📥 接收数据")
        receive_btn.setObjectName("secondaryButton")
        receive_btn.setMinimumHeight(60)
        receive_btn.clicked.connect(self.on_receive_clicked)
        layout.addWidget(receive_btn)
        
        layout.addStretch()
        
        # 返回按钮
        back_btn = QPushButton("← 返回")
        back_btn.setObjectName("secondaryButton")
        back_btn.setMaximumWidth(100)
        back_btn.clicked.connect(self.on_back_clicked)
        layout.addWidget(back_btn)
        
        self.setLayout(layout)
    
    def on_crawler_clicked(self, platform):
        print(f"开始爬取: {platform}")
    
    def on_receive_clicked(self):
        print("接收数据")
    
    def on_back_clicked(self):
        print("返回")
```

### 4. 创建结果展示页

```python
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QTableWidget, 
                             QTableWidgetItem, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class ResultPage(QWidget):
    def __init__(self, data, qr_image_path):
        super().__init__()
        self.data = data
        self.qr_image_path = qr_image_path
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(32, 24, 32, 24)
        layout.setSpacing(16)
        
        # 成功提示
        success_label = QLabel("✅ 爬取成功！")
        success_label.setStyleSheet("font-size: 24px; color: #FFB6C1; font-weight: bold;")
        success_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(success_label)
        
        # 数据表格
        table = self.create_table()
        layout.addWidget(table)
        
        # 二维码和暗号区域
        share_layout = QHBoxLayout()
        share_layout.setSpacing(24)
        
        # 二维码
        qr_widget = self.create_qr_widget()
        share_layout.addWidget(qr_widget)
        
        # 暗号
        code_widget = self.create_code_widget()
        share_layout.addWidget(code_widget)
        
        layout.addLayout(share_layout)
        
        # 倒计时
        timer_label = QLabel("⏰ 有效期：59分58秒")
        timer_label.setStyleSheet("font-size: 16px; color: #666666;")
        timer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(timer_label)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.setSpacing(16)
        
        save_btn = QPushButton("保存Excel")
        save_btn.setMinimumHeight(40)
        save_btn.clicked.connect(self.on_save_clicked)
        button_layout.addWidget(save_btn)
        
        back_btn = QPushButton("返回")
        back_btn.setObjectName("secondaryButton")
        back_btn.setMinimumHeight(40)
        back_btn.clicked.connect(self.on_back_clicked)
        button_layout.addWidget(back_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def create_table(self):
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["排名", "标题", "热度值"])
        table.setRowCount(len(self.data))
        
        # 填充数据
        for row, item in enumerate(self.data):
            table.setItem(row, 0, QTableWidgetItem(str(item['rank'])))
            table.setItem(row, 1, QTableWidgetItem(item['title']))
            table.setItem(row, 2, QTableWidgetItem(str(item['heat'])))
        
        # 设置列宽
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        
        table.setMaximumHeight(300)
        
        return table
    
    def create_qr_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        label = QLabel("二维码")
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        qr_label = QLabel()
        pixmap = QPixmap(self.qr_image_path)
        qr_label.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio))
        layout.addWidget(qr_label)
        
        widget.setLayout(layout)
        return widget
    
    def create_code_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        label = QLabel("暗号")
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        code_label = QLabel("ABC123")
        code_label.setStyleSheet("""
            font-size: 32px; 
            font-weight: bold; 
            color: #FFB6C1;
            font-family: 'Consolas', 'Courier New';
            padding: 16px;
            background-color: #FFF0F5;
            border-radius: 8px;
        """)
        code_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(code_label)
        
        copy_btn = QPushButton("复制")
        copy_btn.setMaximumWidth(100)
        copy_btn.clicked.connect(self.on_copy_clicked)
        layout.addWidget(copy_btn)
        
        widget.setLayout(layout)
        return widget
    
    def on_save_clicked(self):
        print("保存Excel")
    
    def on_back_clicked(self):
        print("返回")
    
    def on_copy_clicked(self):
        from PyQt5.QtWidgets import QApplication
        clipboard = QApplication.clipboard()
        clipboard.setText("ABC123")
        print("已复制到剪贴板")
```

### 5. 主窗口（页面切换）

```python
from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("面对面传输工具")
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(600, 400)
        
        # 应用样式
        self.setStyleSheet(MAIN_STYLESHEET)
        
        # 创建堆叠窗口
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # 添加页面
        self.home_page = HomePage()
        self.function_page = FunctionListPage()
        
        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.function_page)
        
        # 连接信号
        self.home_page.start_btn.clicked.connect(self.show_function_page)
        self.function_page.back_btn.clicked.connect(self.show_home_page)
    
    def show_home_page(self):
        self.stacked_widget.setCurrentWidget(self.home_page)
    
    def show_function_page(self):
        self.stacked_widget.setCurrentWidget(self.function_page)
```

## 常用工具函数

```python
# utils/ui_helpers.py

from PyQt5.QtWidgets import QMessageBox, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPointF

def show_success_message(parent, title, message):
    """显示成功消息框"""
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setStyleSheet("""
        QMessageBox {
            background-color: white;
        }
        QMessageBox QPushButton {
            background-color: #FFB6C1;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 8px 24px;
            min-width: 80px;
        }
        QMessageBox QPushButton:hover {
            background-color: #FFD1DC;
        }
    """)
    msg.exec_()

def show_error_message(parent, title, message):
    """显示错误消息框"""
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.exec_()

def add_shadow(widget, blur=8, offset=(0, 2), color='#FFB6C1', opacity=0.3):
    """为控件添加阴影效果"""
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(blur)
    shadow.setOffset(QPointF(offset[0], offset[1]))
    shadow_color = QColor(color)
    shadow_color.setAlphaF(opacity)
    shadow.setColor(shadow_color)
    widget.setGraphicsEffect(shadow)
```

## 完整项目结构示例

```
src/
├── main.py                 # 应用入口
├── ui/
│   ├── __init__.py
│   ├── main_window.py      # 主窗口
│   ├── home_page.py        # 主页
│   ├── function_list.py    # 功能列表
│   ├── crawling_page.py    # 爬取中
│   └── result_page.py      # 结果页
├── resources/
│   ├── styles.py           # 样式表
│   └── icons/              # 图标
└── utils/
    └── ui_helpers.py       # UI工具函数
```
