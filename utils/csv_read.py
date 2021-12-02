import pandas as pd


# Функция считывания CSV файла
def csv_reader():
    with open('static/csv/netflix.csv') as file:
        result = pd.read_csv(file)
    return result

# Функция получения списка рейтингов
def get_rating_list():
    rating_list = []
    rating_list.append('Все')
    for genre in csv_reader()['rating']:
        if genre not in rating_list:
            rating_list.append(genre)
    return rating_list

def get_genre_list():
    genre_list = []
    genre_list.append('Все')
    for genre in csv_reader()['listed_in']:
        genre = genre.split(',', 1)[0]
        if genre not in genre_list:
            genre_list.append(genre)
    return genre_list






