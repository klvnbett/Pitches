from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password atribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'

class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    users = db.relationship('User', backref='comment', lazy="dynamic")

class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255), nullable=False)