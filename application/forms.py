from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from application.utils import *

class FilterForm(FlaskForm):
    title = StringField('Название: ')
    type = SelectField('Тип: ', choices=[('Все', 'Все'), ('TV Show', 'Сериалы'), ('Movie', 'Фильмы')])
    year = StringField('Год: ')
    rating = SelectField('Рейтинг', choices=get_rating_list())
    genre = SelectField('Жанр', choices=get_genre_list())
    len = SelectField('Кол-во результатов: ', choices=[(10, '10'), (25, '25'), (50, '50'), (100, '10'), ])
    submit = SubmitField('Поиск')

class LoginForm(FlaskForm):
    login = StringField('Login: ')
    password = PasswordField('Пароль: ')
    submit = SubmitField('Войти')