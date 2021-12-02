from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from flask_login import LoginManager

app = Flask(__name__)

# Подключение БД к app (Flask)
app.config.from_object(config.DB_URI)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = config.BaseConfig.SECRET_KEY
db = SQLAlchemy(app)    # Присвоение модуля SQLAlchemy переменной

manager = LoginManager(app)


from . import views
from .utils import *

