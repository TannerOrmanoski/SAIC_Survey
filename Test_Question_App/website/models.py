from turtle import title
from . import db
from flask_login import UserMixin


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    title = db.Column(db.String(150))
    role = db.Column(db.String(150))
    reports_to = db.Column(db.String(150))
    fun_fact = db.Column(db.String(10000))


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
