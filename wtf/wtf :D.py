from flask import Flask
import pandas as pd
from config import *
from flask_sqlalchemy import SQLAlchemy


# Открываем файл static с помощью pandas
def csv_reader():
    with open('../static/csv/netflix.csv') as file:
        df = pd.read_csv(file)
    return df

# Инициализация приложения Flask
app = Flask(__name__)

# Подключение БД к приложению Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{pg_user_name}:{pg_user_pw}@{pg_server}/{pg_db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)    # Присвоение модуля SQLAlchemy переменной

class movies(db.Model):
    show_id = db.Column(db.String(50), primary_key=True)
    type = db.Column(db.String(25))
    title = db.Column(db.Text())
    director = db.Column(db.Text())
    cast = db.Column(db.Text())
    country = db.Column(db.String(100))
    date_added = db.Column(db.String(30))
    release_year = db.Column(db.Integer())
    rating = db.Column(db.String(10))
    duration = db.Column(db.String(20))
    listed_in = db.Column(db.String(200))
    description = db.Column(db.Text())

df = csv_reader()

def films_add():
    movie = []
    for element in all_movies.itertuples():
        movie = movies(show_id = element.show_id,
                       type = element.type,
                       title = element.title,
                       director = element.director,
                       cast = element.cast,
                       country = element.country,
                       date_added = element.date_added,
                       release_year = element.release_year,
                       rating = element.rating,
                       duration = element.duration,
                       listed_in = element.listed_in,
                       description = element.description
                       )
        try:
            db.session.add(movie)
            db.session.commit()
        except:
            print('error')

if __name__ == '__main__':
    app.run(debug=True)

