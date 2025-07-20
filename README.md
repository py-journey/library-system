# 📚 Flask 图书馆管理系统

这是一个基于 **Flask + MySQL + Jinja2 模板引擎** 构建的图书馆管理系统，采用前后端不分离架构。用户可在网页中完成书籍的添加、编辑、删除、注册与登录等操作。

---

## 🛠 技术栈

- **后端框架**：Flask
- **模板引擎**：Jinja2（Flask 默认支持）
- **数据库**：MySQL（或支持的其他关系型数据库）
- **ORM**：SQLAlchemy + Flask-Migrate
- **前端**：HTML + CSS（由后端渲染）
- **架构模式**：前后端不分离（模板渲染）

---

## 📂 项目结构

Library_System/
├── app/
│ ├── templates/ # Jinja2 模板页面
│ │ ├── index.html # 主页
│ │ ├── home.html # 用户主页
│ │ ├── edit.html # 编辑图书
│ │ ├── login.html # 登录页面
│ │ └── register.html # 注册页面
│ ├── init.py # Flask 应用工厂
│ ├── exts.py # 扩展（如 db, migrate 初始化）
│ ├── models.py # 数据库模型：Book, Author, User
│ └── views.py # 路由视图函数
│
├── migrations/ # Flask-Migrate 自动生成的迁移文件
│ ├── versions/ # 每次迁移的版本文件
│ ├── env.py # 迁移配置文件
│ └── alembic.ini # Alembic 配置文件
│
├── myenv/ # 虚拟环境（不建议上传到 GitHub）
├── librarydb.sql # 数据库导出文件（可选）
├── run.py # 程序入口
└── README.md # 项目说明文档

---

## 1. 克隆项目

git clone git@github.com:py-journey/library-system.git
cd library-system

## 2. 创建虚拟环境并安装依赖
python -m venv myenv
# Windows: myenv\Scripts\activate
# Linux: source myenv/bin/activate 

## 3. 启动服务
flask run
默认访问地址：http://127.0.0.1:5000

