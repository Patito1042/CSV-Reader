# CSV Reader

The work was performed as a test task

What does
- Collects data from a csv file
- Writes data to the database
- Outputs data to a web application

Functionality
- Authorization
- Search filters

Frameworks used
- Flask
- Pandas
- SQLAlchemy

The database used postgres

## Add a new search filter

1. You need to access the search function and add a filter.
> application/utils/search_module.py
````python
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
````

2. Add a new form
> application/forms.py
````python
class FilterForm(FlaskForm):
    title = StringField('Название: ')
    type = SelectField('Тип: ', choices=[('Все', 'Все'), ('TV Show', 'Сериалы'), ('Movie', 'Фильмы')])
    year = StringField('Год: ')
    rating = SelectField('Рейтинг', choices=get_rating_list())
    genre = SelectField('Жанр', choices=get_genre_list())
    len = SelectField('Кол-во результатов: ', choices=[(10, '10'), (25, '25'), (50, '50'), (100, '10'), ])
    submit = SubmitField('Поиск')
````

3. Add variables to the view
> application/views.py
````python
def search():
    ...
    # Значения поиска по умолчанию
    type, title, year, rating, genre = '', '', '', '', ''
    ...
    if form.is_submitted():
        type = form.type.data
        year = form.year.data
        title = form.title.data
        rating = form.rating.data
        genre = form.genre.data
    ...
    search_result = search_movie(type=type,
                             title=title,
                             release_year=year,
                             rating=rating,
                             genre=genre
                             )[0:count]
````
