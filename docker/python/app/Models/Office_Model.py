from app import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Office(db.Model, UserMixin):
    __tablename__ = 'office'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(120), unique=True, nullable=False)
    call_number = db.Column(db.String(15), unique=True, nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._password, password)
