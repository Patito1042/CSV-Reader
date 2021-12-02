from application import db
from ..models import Movies
from sqlalchemy import and_

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