from marshmallow import Schema, fields, validate


class UserSchema(Schema):

    id = fields.Integer()
    email = fields.String(allow_none=False, validate=validate.Email())
    password = fields.String(allow_none=False, validate=validate.Length(min=8, max=20))


user_request_schema = UserSchema(only=('email', 'password'))
user_response_schema = UserSchema(only=('id', 'email'))
