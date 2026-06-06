# 面对面传输工具

一个简洁美观的热搜爬虫和数据分享工具。

## 项目状态

🚧 **开发中** - 第一阶段已完成

### 已完成功能
- ✅ 项目结构搭建
- ✅ Python环境配置
- ✅ PyQt5界面框架
- ✅ 主页UI（白色+粉色主题）
- ✅ 全局样式表
- ✅ Hello World演示

### 开发中功能
- 🔄 功能列表页
- 🔄 爬虫功能
- 🔄 数据分享功能

## 快速开始

### 环境要求
- Python 3.10+
- Windows 10/11

### 安装依赖

```bash
# 安装PyQt5（系统级）
py -m pip install PyQt5

# 或使用虚拟环境
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 运行应用

**方法1：使用批处理文件（推荐）**
```bash
run.bat
```

**方法2：直接运行**
```bash
cd src
py main.py
```

## 项目结构

```
面对面传输/
├── src/                    # 源代码
│   ├── main.py            # 主程序入口
│   ├── config.py          # 配置文件
│   ├── ui/                # 界面模块
│   │   ├── main_window.py # 主窗口
│   │   └── home_page.py   # 主页
│   ├── crawler/           # 爬虫模块（待开发）
│   ├── utils/             # 工具模块（待开发）
│   └── resources/         # 资源文件
│       └── styles.qss     # 样式表
├── server/                # 数据分享服务器（待开发）
├── docs/                  # 项目文档
├── dev-logs/              # 开发日志
├── requirements.txt       # Python依赖
└── run.bat               # 启动脚本

```

## 技术栈

- **GUI框架：** PyQt5
- **爬虫：** requests + BeautifulSoup + Selenium
- **Excel：** openpyxl
- **二维码：** qrcode
- **后端：** Flask + SQLite
- **打包：** PyInstaller

## 设计规范

- **配色：** 白色 + 暖粉色 (#FFB6C1)
- **字体：** 微软雅黑
- **风格：** 简洁、清晰、易用

## 开发计划

详见 [开发计划文档](docs/03-开发计划与步骤.md)

- [x] 第一阶段：项目初始化（已完成）
- [ ] 第二阶段：界面开发
- [ ] 第三阶段：爬虫功能
- [ ] 第四阶段：本地存储
- [ ] 第五阶段：分享服务器
- [ ] 第六阶段：二维码暗号
- [ ] 第七阶段：数据接收
- [ ] 第八阶段：错误处理
- [ ] 第九阶段：打包测试
- [ ] 第十阶段：文档交付

## 文档

- [项目需求文档](docs/01-项目需求文档.md)
- [技术选型文档](docs/02-技术选型文档.md)
- [开发计划与步骤](docs/03-开发计划与步骤.md)
- [设计规范](docs/04-设计规范.md)
- [环境安装指南](docs/00-环境安装指南.md)

## 开发日志

查看 [dev-logs](dev-logs/) 目录

## 许可证

MIT License

## 作者

面对面传输工具开发团队

---

**版本：** 1.0.0-alpha  
**最后更新：** 2026-05-16
