# -*- coding: utf-8 -*-
"""
配置文件 - 颜色、字体、尺寸等常量
"""

# 颜色配置
COLORS = {
    # 主背景色
    'bg_primary': '#FFFFFF',
    
    # 主题色 - 暖粉色系（加深以提升对比度）
    'color_primary': '#E0687A',
    'color_primary_light': '#F0909B',
    'color_primary_dark': '#C85568',

    # 辅助色
    'color_secondary': '#FFF0F3',
    'color_accent': '#D05575',

    # 文字颜色
    'text_primary': '#333333',
    'text_secondary': '#666666',
    'text_disabled': '#CCCCCC',
    'text_white': '#FFFFFF',

    # 状态色
    'color_success': '#E0687A',
    'color_error': '#D05575',
    'color_warning': '#F0909B',
    'color_info': '#FFF0F3',

    # 边框和分割线
    'border_color': '#F0B0B8',
    'divider_color': '#FFF0F3',
}

# 字体配置
FONT_FAMILY = "Microsoft YaHei, 微软雅黑, SimHei, 黑体, Arial"

FONT_SIZES = {
    'xs': 12,
    'sm': 14,
    'base': 16,
    'lg': 18,
    'xl': 24,
    'xxl': 32,
    'hero': 48,
}

# 间距配置
SPACING = {
    'xs': 4,
    'sm': 8,
    'md': 16,
    'lg': 24,
    'xl': 32,
    'xxl': 48,
}

# 圆角配置
RADIUS = {
    'sm': 4,
    'md': 8,
    'lg': 12,
    'xl': 16,
}

# 窗口配置
WINDOW_CONFIG = {
    'default_width': 860,
    'default_height': 680,
    'min_width': 640,
    'min_height': 480,
}

# 应用信息
APP_NAME = "面对面热搜爬虫工具"
APP_VERSION = "1.0.0"
