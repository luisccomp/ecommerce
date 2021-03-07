from flask import Blueprint, request, jsonify
from marshmallow.validate import ValidationError

from ecommerce.models.categories import CategoryRequestSchema
from ecommerce.services import categories_service

router = Blueprint('categories', __name__)


@router.route('/api/categories', methods=['POST'])
def create_category():
    try:
        # To avoid overposting issues, just get only the data needed to create a category on database.
        schema = CategoryRequestSchema(only=('name',))
        category_create_request = schema.load(request.json)

        return categories_service.create_category(category_create_request), 201
    except ValidationError as e:
        return {
            'status': 400,
            'message': 'Validation error',
            'details': e.messages
        }, 400


@router.route('/api/categories', methods=['GET'])
def find_all_categories():
    # Return all categories stored on database as a list.
    return jsonify(categories_service.find_all_categories())


@router.route('/api/categories/<int:category_id>', methods=['GET'])
def find_category_by_id(category_id):
    # Return a category from database
    return categories_service.find_category_by_id(category_id)


@router.route('/api/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    # Updates a category on database
    try:
        schema = CategoryRequestSchema(only=('name',))
        category_update_request = schema.load(request.json)

        return categories_service.update_category(category_id, category_update_request)
    except ValidationError as e:
        return {
            'status': 400,
            'message': 'Validation error',
            'details': e.messages
        }, 400


@router.route('/api/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    # Delete a category from database
    categories_service.delete_category(category_id)

    return jsonify(), 204
