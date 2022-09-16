import http
from flask import Blueprint, jsonify, request
from models.authors import Authors
from database import db
from serializers.authors import AuthorsSchema
from marshmallow import ValidationError

authors_router = Blueprint('authors', __name__, url_prefix='/authors')


@authors_router.route('')
def get():
    all_authors = Authors.query.all()
    authors_json = AuthorsSchema().dump(all_authors, many=True)
    return jsonify(authors_json), http.HTTPStatus.OK


@authors_router.route('/<int:id_>')
def retrieve(id_):
    author = Authors.query.filter(Authors.authors_id == id_).first()
    author_json = AuthorsSchema().dump(author)
    return jsonify(author_json), http.HTTPStatus.OK


@authors_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)
    try:
        data_json = AuthorsSchema().load(data)
        new_author = Authors(name_surname=data_json["name_surname"])
        db.session.add(new_author)
        db.session.commit()
        new_book_json = AuthorsSchema().dump(new_author)
    except ValidationError as e:
        return {'Errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return jsonify(new_book_json), http.HTTPStatus.CREATED


@authors_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Authors.query.filter(Authors.authors_id == id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT


@authors_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)
    try:
        data_json = AuthorsSchema().load(data)
        author = Authors.query.filter(Authors.authors_id == id_).first()
        author.name_surname = data_json["name_surname"]
        db.session.add(author)
        db.session.commit()
        new_author_json = AuthorsSchema().dump(author)
    except ValidationError as e:
        return {'Errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return jsonify(new_author_json), http.HTTPStatus.OK
