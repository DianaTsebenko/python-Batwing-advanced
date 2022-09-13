import http
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from database import db
from models.books import Book
from serializers.books import BookSchema

books_router = Blueprint('book', __name__, url_prefix='/book')


@books_router.route('')
def get():
    book_schema = BookSchema()
    books = Book.query.order_by(Book.title)
    book_json = book_schema.dump(books, many=True)
    return jsonify(book_json)


@books_router.route('/<int:id_>')
def retrieve(id_):
    book_schema = BookSchema()
    book = Book.query.filter_by(id=id_).first()
    book_json = book_schema.dump(book)
    return jsonify(book_json)


@books_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)
    book_schema = BookSchema()
    try:
        book_data = book_schema.load(data)
        new_book = Book(title=book_data['title'], writer=book_data['writer'])
        db.session.add(new_book)
        db.session.commit()
        new_book_json = book_schema.dump(new_book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_book_json


@books_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)
    book_schema = BookSchema()
    try:
        book_data = book_schema.load(data)
        upd_book = Book.query.filter_by(id=id_).first()
        upd_book.title = book_data['title']
        upd_book.writer = book_data['writer']
        db.session.commit()
        book_json = book_schema.dump(upd_book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return book_json


@books_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    try:
        del_book = Book.query.filter_by(id=id_).first()
        db.session.delete(del_book)
        db.session.commit()
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return {}, http.HTTPStatus.NO_CONTENT