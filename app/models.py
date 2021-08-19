from datetime import datetime
from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True, nullable=False)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    comment = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    pitch = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
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
    user_id= db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    pitch_id= db.Column(db.Integer,db.ForeignKey('pitches.id'), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))

class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    comment = db.relationship('Comment', backref='pitch', lazy='dynamic')
    
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_category = db.Column(db.String)
    pitch_comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)

    

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, category):
        pitches = Pitch.query.filter_by(pitch_category=category).all()
        return pitches

    @classmethod
    def getPitchId(cls, id):
        pitch = Pitch.query.filter_by(id=id).first()
        return pitch