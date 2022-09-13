import http
from flask import Blueprint, Response, request, jsonify, make_response
from db.db_books import BookDB

book_router = Blueprint('book', __name__, url_prefix='/book')
db = BookDB()


@book_router.route('')
def get():
    books = db.get_all()
    return jsonify(books)


@book_router.route('/<string:title>')
def retrieve(title):
    book = db.retrieve(title)
    if book is None:
        return title + " - NOT FOUND!", http.HTTPStatus.NOT_FOUND
    return book


@book_router.route('', methods=['POST'])
def create():
    title = request.json.get("title")
    author = request.json.get("author")
    description = request.json.get("description")
    new_book = db.add(title, author, description)
    if new_book is None:
        return 'A book with this title already exists.', http.HTTPStatus.NOT_ACCEPTABLE
    return new_book, http.HTTPStatus.CREATED


@book_router.route('', methods=['PUT'])
def update():
    title = request.json.get("title")
    author = request.json.get("author")
    description = request.json.get("description")
    update_book = db.update(title, author, description)
    if update_book is None:
        return 'A book with this title not found.', http.HTTPStatus.BAD_REQUEST
    return update_book, http.HTTPStatus.ACCEPTED


@book_router.route('/<string:title>', methods=['DELETE'])
def delete(title):
    db.delete(title)
    return {}, http.HTTPStatus.NO_CONTENT
