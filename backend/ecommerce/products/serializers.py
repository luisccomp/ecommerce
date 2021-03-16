from marshmallow import Schema, fields, validate
from ecommerce.categories.serializers import category_response_schema


class ProductSchema(Schema):

    id = fields.Integer()
    name = fields.String(allow_none=False, required=True, validate=validate.Length(min=3, max=50))
    description = fields.String(allow_none=False, required=True, validate=validate.Length(max=255))
    category_id = fields.Integer(required=True)
    category = fields.Nested(category_response_schema)


product_request_schema = ProductSchema(only=('name', 'description', 'category_id'))
product_response_schema = ProductSchema(only=('id', 'name', 'description', 'category'))
products_response_schema = ProductSchema(many=True, only=('id', 'name', 'description'))
