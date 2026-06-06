# 面对面传输工具 🚀

> 简洁美观的热搜爬虫 + 面对面数据分享工具

## 项目状态

✅ **已完成** — v1.0

---

## 功能

### 🔥 热搜爬虫
- 微博热搜
- 抖音热点
- B站热门
- 支持 Cookie 登录，绕过反爬

### 📊 数据展示
- 热门榜单实时查看
- 数据导出 Excel

### 📲 面对面分享
- 本地 Flask 服务器
- 二维码扫码接收数据
- 局域网直连，数据不出网

### 🎨 界面
- PyQt5 桌面应用
- 白色 + 暖粉色主题
- 4 个页面：主页 / 爬取 / 结果 / 分享

---

## 快速开始

### 环境要求
- Python 3.10+
- Windows 10/11

### 安装

```bash
# 创建虚拟环境
python -m venv venv
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 运行

```bash
run.bat
```

或者

```bash
python -m src.main
```

### 打包

```bash
pyinstaller HotSearchTool.spec
```

---

## 项目结构

```
share_tool/
├── src/
│   ├── main.py              # 程序入口
│   ├── config.py            # 配置
│   ├── ui/                  # 界面
│   │   ├── main_window.py   # 主窗口
│   │   ├── home_page.py     # 主页
│   │   ├── function_list_page.py  # 功能列表
│   │   ├── crawling_page.py # 爬取页面
│   │   └── result_page.py   # 结果页面
│   ├── crawler/             # 爬虫
│   │   ├── base.py          # 基础爬虫
│   │   ├── weibo.py         # 微博爬虫
│   │   ├── douyin.py        # 抖音爬虫
│   │   ├── bilibili.py      # B站爬虫
│   │   └── cookies.py       # Cookie 管理
│   ├── utils/               # 工具
│   │   ├── storage.py       # 本地存储
│   │   ├── excel_handler.py # Excel 导出
│   │   ├── qr_generator.py  # 二维码生成
│   │   └── share_service.py # 分享服务
│   └── resources/
│       └── styles.qss       # 样式表
├── server/                  # Flask 分享服务器
│   ├── app.py
│   ├── database.py
│   └── cleanup.py
├── docs/                    # 项目文档
├── dev-logs/                # 开发日志
├── requirements.txt
└── run.bat
```

---

## 技术栈

| 模块 | 技术 |
|------|------|
| GUI | PyQt5 |
| 爬虫 | requests + BeautifulSoup + Selenium |
| Excel | openpyxl |
| 二维码 | qrcode |
| 后端 | Flask + SQLite |
| 打包 | PyInstaller |

---

## 设计

- **配色：** 白色 + 暖粉色 `#FFB6C1`
- **字体：** 微软雅黑
- **风格：** 简洁清晰，小白友好

---

## 文档

- [项目需求](docs/01-项目需求文档.md)
- [技术选型](docs/02-技术选型文档.md)
- [开发计划](docs/03-开发计划与步骤.md)
- [设计规范](docs/04-设计规范.md)
- [环境安装](docs/00-环境安装指南.md)

---

## 许可证

MIT License

---

**版本：** 1.0.0  
**最后更新：** 2026-06-06
