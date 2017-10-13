from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, DateTimeField, FloatField, BooleanField, DateField, \
    SelectField
from wtforms.validators import DataRequired, Length


class BillerForm(FlaskForm):
    account = IntegerField('account', validators=[DataRequired()])
    amount = IntegerField('amount', validators=[DataRequired()])


class ScheduleForm(FlaskForm):
    biller = SelectField('biller', validators=[DataRequired()],
                         choices=[('zesa', 'ZESA'), ('coh', 'City Of Harare'), ('zol', 'ZOL'), ('telone', 'TelOne')])
    service_account = IntegerField('account', validators=[DataRequired()])
    frequency = SelectField('frequency', validators=[DataRequired()],
                            choices=[('week', 'Weekly'), ('month', 'Monthly'), ('year', 'Yearly')])
    test_select = SelectField('testselect', choices=[('item1', 'Item 1'), ('item2', 'Item 2')])
    start_date = DateField('start_date', validators=[DataRequired()])
    amount = FloatField('amount', validators=[DataRequired()])
    accept_toc = BooleanField('terms', validators=[DataRequired()])
