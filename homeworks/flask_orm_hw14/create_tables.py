from main import db
from models.user import User
from models.books import Book

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    db.session.add(User(email="diana@gmail.com"))
    db.session.commit()
    db.session.add(Book(book_name="Name"))
    db.session.commit()
    print("created tables")
