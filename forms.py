from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from models import Countrys


class CompanyForm(FlaskForm):
    name = StringField('Название компании', validators=[DataRequired()])
    ynp = StringField('УНП', validators=[DataRequired()])
    comment = TextAreaField('Коментарий')
    bank_name = StringField('Название бака')
    bank_account = IntegerField('Номер счета')
    email = StringField('Email', validators=[Email()])
    # country = StringField('Страна')
    country = SelectField('Страна', choices=Countrys.query.all())