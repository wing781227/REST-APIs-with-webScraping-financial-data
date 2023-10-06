from marshmallow import Schema, fields


class StockSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    stats = fields.List(required=True)
    price = fields.Float(required=True)

class StockUpdateSchema(Schema):
    stats = fields.List()
    price = fields.Float()

