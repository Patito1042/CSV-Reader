from flask_login import UserMixin, login_manager

from application import db, manager


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

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    pass

@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)