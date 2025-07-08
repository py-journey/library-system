# flask应用
from flask import Flask

from app.exts import init_exts

from app.models import *

from app.views import main


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'sdlaghkahj123456'  # 替换为随机字符串


    # 配置蓝图
    app.register_blueprint(blueprint=main)

    # mysql数据库
    db_uri = 'mysql+pymysql://root:root@localhost:3306/librarydb?charset=utf8mb4'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLCHEMY_TRACE_MODIFICATIONS'] = False
    # 初始化第三方插件
    init_exts(app)

    return app