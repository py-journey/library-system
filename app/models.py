# 数据模型
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref

from .exts import *
# 用户表
class User(db.Model):
    # 表名
    __tablename__ = 'user'
    # 字段名
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20))
    passwd = db.Column(db.Integer)

# 作者表
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)

    books = db.relationship('Book',backref='author',lazy=True)

class Book(db.Model):
    # 表名
    __tablename__ = 'book'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20))
    # 外键约束
    author_id = db.Column(db.Integer,ForeignKey('author.id'))


