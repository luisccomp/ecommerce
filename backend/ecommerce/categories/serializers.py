from marshmallow import Schema, fields, pre_load, post_dump, validate


class CategorySchema(Schema):

    id = fields.Integer()
    name = fields.String(allow_none=False, required=True, validate=validate.Length(min=1, max=50))


category_schema = CategorySchema(only=('name',))
category_response_schema = CategorySchema(only=('id', 'name'))
category_schemas = CategorySchema(many=True)
