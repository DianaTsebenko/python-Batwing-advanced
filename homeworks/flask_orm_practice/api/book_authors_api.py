import http
from flask import Blueprint, jsonify, request
from models.book_authors import BookAuthors
from models.book import Book
from models.authors import Authors
from database import db
from serializers.book_authors import BookAuthorsSchema

book_authors = Blueprint("book_authors", __name__, url_prefix='/book_authors')


@book_authors.route('')
def get():
    ba_all = BookAuthors.query.all()
    ba_json = BookAuthorsSchema().dump(ba_all, many=True)
    return jsonify(ba_json)


@book_authors.route('/<int:id_>')
def retrieve(id_):
    ba = BookAuthors.query.filter_by(id=id_).first()
    ba_json = BookAuthorsSchema().dump(ba)
    return jsonify(ba_json)


@book_authors.route('/<int:book_id>/<int:author_id>', methods=['POST'])
def create(book_id, author_id):
    if Book.query.filter(Book.book_id == book_id).first() and Authors.query.filter(
            Authors.authors_id == author_id).first():
        new_relation = BookAuthors(book_id=book_id, author_id=author_id)
        db.session.add(new_relation)
        db.session.commit()
        new_relation_json = BookAuthorsSchema().dump(new_relation)
        return jsonify(new_relation_json), http.HTTPStatus.CREATED
    else:
        return 'BAD ID', http.HTTPStatus.BAD_REQUEST


@book_authors.route('', methods=['PUT'])
def update():
    data = request.get_json(force=True)

    if ba := BookAuthors.query.filter_by(id=data["id"]).first():
        ba.book_id, ba.author_id = data["book_id"], data["author_id"]
        db.session.add(ba)
        db.session.commit()
        new_ba = BookAuthorsSchema().dump(ba)
        return jsonify(new_ba)
    else:
        return 'BAD ID', http.HTTPStatus.BAD_REQUEST


@book_authors.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    BookAuthors.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
