from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from models import Countrys


class CompanyForm(FlaskForm):
    name = StringField('Название контрагента', validators=[DataRequired()])
    main_phone = StringField('Основной телефон')
    second_phone = StringField('Дополнительный телефон')
    email = StringField('Email', validators=[Email()])
    second_email = StringField('Дополнительный Email', validators=[Email()])
    ynp = StringField('УНП', validators=[Length(min=2,max=9)])
    rating = IntegerField('Рейтинг', validators=[DataRequired()])
    web = StringField('Веб адрес')
    industry = StringField('Отрасль компании')
    comment = TextAreaField('Коментарий')
    bank_name = StringField('Название банка')
    bank_account = StringField('Номер счета')
    country = SelectField('Страна', choices=Countrys.query.all())
    company_adr = TextAreaField('Адрес')
    submit = SubmitField('Добавить')