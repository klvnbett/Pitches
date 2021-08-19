from wtforms import StringField,TextAreaField, SubmitField, SelectField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class PitchForm(FlaskForm):
    pitch_title = StringField('Pitch title', validators=[Required()])
    pitch_category = SelectField('Pitch category',choices=[('Select a category','Select a category'),('Product','Product'),('Promotions','Promotions'),('Business','Business'),('Pickup lines', 'Pickup lines')], validators=[Required()])
    pitch_comment = StringField('What is in your mind?')
    submit = SubmitField('Pitch')
    
class Comment(FlaskForm):
    comment = TextAreaField('What do you think about this?', validators=[Required()])
    submit = SubmitField('Send')