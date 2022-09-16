from database import db


class BookAuthors(db.Model):
    __tablename__ = 'book_authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.book_id"))
    author_id = db.Column(db.Integer, db.ForeignKey("authors.authors_id"))
    books = db.relationship("Book")
    authors = db.relationship("Authors")
