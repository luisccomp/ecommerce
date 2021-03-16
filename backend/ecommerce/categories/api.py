from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required
from marshmallow.exceptions import ValidationError
from .models import Category
from .serializers import category_schema, category_schemas, category_response_schema
from ecommerce.exceptions import HttpError

blueprint = Blueprint('categories', __name__)


@blueprint.route('/api/categories', methods=('POST',))
@jwt_required()
def create_category():
    try:
        category_create_request = category_schema.load(data=request.json)
        category = Category.create(**category_create_request)

        response = category_response_schema.dump(category)

        return response, 201
    except ValidationError as e:
        raise HttpError.bad_request(message='Validation error', details=e.messages)


@blueprint.route('/api/categories', methods=('GET',))
def find_all_categories():
    categories = Category.query.all()
    categories = category_schemas.dump(categories)

    return jsonify(categories)


@blueprint.route('/api/categories/<int:category_id>')
def find_category_by_id(category_id):
    category = Category.query.get(category_id)

    if category is None:
        raise HttpError.not_found('Category not found')

    return category_response_schema.dump(category)


@blueprint.route('/api/categories/<int:category_id>', methods=('PUT',))
@jwt_required()
def update_category(category_id):
    try:
        category_update_request = category_schema.load(data=request.json)
        category = Category.query.get(category_id)

        if category is None:
            raise HttpError.not_found('Category not found')

        category.updated_at = datetime.utcnow()
        category = category.update(**category_update_request)

        return category_response_schema.dump(category)
    except ValidationError as e:
        raise HttpError.bad_request(message='Validation error', details=e.messages)


@blueprint.route('/api/categories/<int:category_id>', methods=('DELETE',))
@jwt_required()
def delete_category(category_id):
    category = Category.query.get(category_id)

    if category is None:
        raise HttpError.not_found('Category not found')

    category.delete()

    return jsonify(), 204
