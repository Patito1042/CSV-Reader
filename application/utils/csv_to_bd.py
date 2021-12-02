from sqlalchemy import create_engine
from . import csv_reader
from config import DB_URI

# Запись CSV в БД
def csv_into_bd():
    try:
        engine = create_engine(DB_URI.SQLALCHEMY_DATABASE_URI)
        df = csv_reader()
        df.to_sql('movies', engine, if_exists='append', schema=None, index=False)
    except:
        print('csv_into_bd error')