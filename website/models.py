from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# create a product class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    price = db.Column(db.Integer)
    description = db.Column(db.String(10000))
    image = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())


# create a user class
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
