from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    username = StringField('Enter your username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class UpdateProfileForm(FlaskForm):
    bio=TextAreaField('Tell us about you', validators=[Required()])
    submit = SubmitField('Submit')

class Pitch(FlaskForm):
    pitch_title = StringField('Pitch title', validators=[Required()])
    pitch_group = StringField('Pitch category',choices=[('Select a category','Select a category'),('Product','Product'),('Promotions','Promotions'),('Business','Business'),('Pickup lines', 'Pickup lines')], validators=[Required()])
    pitch_comment = StringField('What is in your mind?')
    submit = SubmitField('Pitch')
    
class Comment(FlaskForm):
    comment = TextAreaField('What do you think about this?', validators=[Required()])
    submit = SubmitField('Send')