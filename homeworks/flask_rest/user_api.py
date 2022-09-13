import http

from flask import Blueprint, Response, request, jsonify, make_response

from db.db import UserDB

user_router = Blueprint('user', __name__, url_prefix='/user')
db = UserDB()


@user_router.route('')
def get():
    users = jsonify(db.get_all())
    return users


@user_router.route('/<string:email>')
def retrieve(email):
    user = db.retrieve_by_email(email)
    if user is None:
        return email, http.HTTPStatus.NOT_FOUND
    return user


@user_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    new_user = db.add(name, email, password)
    if new_user is None:
        return 'A user with this email already exists.', http.HTTPStatus.NOT_ACCEPTABLE
    return new_user, http.HTTPStatus.CREATED


@user_router.route('', methods=['PUT', 'PATCH'])
def update():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    update_user = db.update_by_email(name, email, password)
    if update_user is None:
        return 'A user with this email not found.', http.HTTPStatus.BAD_REQUEST
    return update_user, http.HTTPStatus.ACCEPTED


@user_router.route('/<string:email>', methods=['DELETE'])
def delete(email):
    db.delete_by_email(email)
    return {}, http.HTTPStatus.NO_CONTENT
