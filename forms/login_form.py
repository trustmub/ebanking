from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, DateField, SelectField, PasswordField
from wtforms.validators import DataRequired, InputRequired


class LoginForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    idType = SelectField('idType', validators=[DataRequired()],
                         choices=[('nid', 'National ID'), ('pass', 'Password Number')])
    idNumber = StringField('idNumber', validators=[InputRequired()])
    dob = DateField('dob', validators=[DataRequired(message="please enter Date Of Birth")])
    accountNumberReg = IntegerField('accountNumberReg', validators=[InputRequired()])
    tndcRegCheck = BooleanField('tndcRegCheck', validators=[DataRequired()])
    otpNumber = IntegerField('otpNumber', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired])
    password = PasswordField('password', validators=[DataRequired])
    password2 = PasswordField('password2', validators=[DataRequired])
