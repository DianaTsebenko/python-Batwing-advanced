from marshmallow import Schema, fields
from serializers.book import BookSchema
from serializers.authors import AuthorsSchema


class BookAuthorsSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    authors = fields.Nested(AuthorsSchema())
    book = fields.Nested(BookSchema())
