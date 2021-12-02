from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, and_
from utils import *
from config import *
from forms import FilterForm

import os

SECRET_KEY = os.urandom(32)

# Инициализация приложения Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

# Подключение БД к Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{pg_user_name}:{pg_user_pw}@{pg_server}/{pg_db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)    # Присвоение модуля SQLAlchemy переменной

# Определение модели фильма
class Movies(db.Model):
    show_id = db.Column(db.String(50), primary_key=True)
    type = db.Column(db.String(25))
    title = db.Column(db.Text())
    director = db.Column(db.Text())
    cast = db.Column(db.Text())
    country = db.Column(db.String(200))
    date_added = db.Column(db.String(30))
    release_year = db.Column(db.String(4))
    rating = db.Column(db.String(10))
    duration = db.Column(db.String(20))
    listed_in = db.Column(db.String(200))
    description = db.Column(db.Text())

    def __repr__(self):
        return f"<movie {self.title}>"

# Создание таблиц БД
db.create_all()

# Запись CSV в БД
def csv_into_bd():
    try:
        engine = create_engine(f'postgresql+psycopg2://{pg_user_name}:{pg_user_pw}@{pg_server}/{pg_db_name}')
        df = csv_reader()
        df.to_sql('movies', engine, if_exists='append', schema=None, index=False)
    except:
        print('csv_into_bd error')

csv_into_bd()

# Получение списка фильмов методом поиска
def search_movie(title='', type='', rating='', release_year='', genre=''):  #
    session = db.session.query(Movies).filter(
        and_(
            Movies.type.like(f'{type}%'),   # сериал/фильм
            Movies.title.ilike(f'%{title}%'),    # Название
            Movies.rating.like(f'{rating}%'),   # Рейтинг
            Movies.release_year.like(f'{release_year}%'),
            Movies.listed_in.like(f'%{genre}%')     # Жанр
        )
            ).all()
    return session

# Получение данных из БД в pandas ???
# engine = create_engine(f'postgresql://{pg_user_name}:{pg_user_pw}@{pg_server}/{pg_db_name}').connect()
# search_in_pd = pd.read_sql_table('movies', engine)

# Представления страницы поиска
@app.route('/', methods=['POST', 'GET'])
def search():

    # Количество результатов на странице
    count = 30000

    # Значения поиска по умолчанию
    type, title, year, rating, genre = '', '', '', '', ''

    #
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

print(get_genre_list())

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=False)