from marshmallow import Schema, fields
from marshmallow.validate import Length


class BookSchema(Schema):
    book_id = fields.Integer(required=True, dump_only=True)
    book_name = fields.String(required=True, validate=Length(min=3, max=355))
