from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
