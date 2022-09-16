from database import db


class Authors(db.Model):
    __tablename__ = 'authors'

    authors_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_surname = db.Column(db.String(300), nullable=False, unique=True)
