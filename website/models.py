from . import db
from flask_login import UserMixin
from sqlalchemy import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(150))
    notes = db.relationship('Note')

