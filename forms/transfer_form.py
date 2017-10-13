from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,PasswordField
from wtforms.validators import DataRequired


class InternalForm(FlaskForm):
    account = IntegerField('account', validators=[DataRequired()])
    amount = IntegerField('amount', validators=[DataRequired()])
