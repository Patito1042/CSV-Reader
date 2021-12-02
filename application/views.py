from flask_login import login_user, login_required, logout_user

from application import app, db
from .forms import FilterForm, LoginForm, RegisterForm
from .models import User
from .utils import search_movie
from flask import render_template, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash

# Представления страницы поиска
@app.route('/', methods=['POST', 'GET'])

def search():
    # Количество результатов на странице
    count = 50
    # Значения поиска по умолчанию
    type, title, year, rating, genre = '', '', '', '', ''
    # Запись данных формы из FilterForm
    form = FilterForm()
    # Проверка get запроса
    if form.is_submitted():
        type = form.type.data
        year = form.year.data
        title = form.title.data
        rating = form.rating.data
        genre = form.genre.data

        if form.rating.data  == 'Все':
            rating = ''
        if form.genre.data == 'Все':
            genre = ''
        if form.type.data == 'Все':
            type = ''

    # Выполнение поиска ()
    search_result = search_movie(type=type,
                                 title=title,
                                 release_year=year,
                                 rating=rating,
                                 genre=genre
                                 )[0:count]

    return render_template('index.html', form=form, search=search_result)

# Представление страницы авторизации
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if not login_required:
        print('hi')
        return redirect('/logout')
    form = LoginForm()
    login = form.login.data
    password = form.password.data

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return render_template('logout.html', form=form)
        else:
            flash('Неверный логин/пароль')

    else:
        flash('Введите логин/пароль')
    return render_template('login.html', form=form)

# Представление страницы регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    login = form.login.data
    password = form.password.data
    password_repeat = form.password_repeat.data
    login_check = User.query.filter_by(login=login).first()

    if form.is_submitted():

        if not (login or password or password_repeat):
            flash('Заполните все поля')

        elif password != password_repeat:
            flash('Пароли не совпадают')

        elif login_check:
            flash('Такой логин уже есть')

        if not login_check:
            hash_pwd = generate_password_hash(password)
            new_user = User(login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')

        return redirect('/register')

    return render_template('register.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required

def logout():
    form = LoginForm()
    if form.is_submitted():
        logout_user()
        return redirect('/login')
    return render_template('logout.html', form=form)


