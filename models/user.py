from setup import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
