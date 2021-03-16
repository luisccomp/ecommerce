from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from .models import User
from .serializers import user_request_schema, user_response_schema
from ecommerce.exceptions import HttpError
from ecommerce.extensions import bcrypt

blueprint = Blueprint('users', __name__)


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    try:
        user = user_request_schema.load(request.json)
        user['password'] = bcrypt.generate_password_hash(user['password'])
        user = User.create(**user)

        return user_response_schema.dump(user), 201
    except ValidationError as ve:
        raise HttpError.bad_request('Validation error', ve.messages)
