# 第三方安装库
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 初始化
db = SQLAlchemy()
migrate = Migrate()

def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)

