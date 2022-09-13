from database import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book = db.Column(db.String, nullable=False, unique=True)