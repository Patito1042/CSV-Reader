from flask_login import login_user
from werkzeug.utils import redirect

from application import app
from .forms import FilterForm, LoginForm
from .models import User
from .utils import search_movie
from flask import render_template
from werkzeug.security import check_password_hash

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

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    login = form.login.data
    password = form.password.data
    print(password), print(login)
    if login and password:
        user = User.query.filter_by(login=login).first()
        if check_password_hash(user.password, password):
            login_user(user)
            redirect('/')
    else:
        return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    pass

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    pass
