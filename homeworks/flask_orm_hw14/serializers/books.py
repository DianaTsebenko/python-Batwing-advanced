from marshmallow import Schema, fields
from marshmallow.validate import Length


class BookSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    book = fields.String(required=True)