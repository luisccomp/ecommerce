from flask import Blueprint, request, jsonify
from marshmallow.exceptions import ValidationError
from flask_jwt import jwt_required
from ecommerce.exceptions import HttpError
from .serializers import product_request_schema, product_response_schema, products_response_schema
from .models import Product

blueprint = Blueprint('products', __name__)


@blueprint.route('/api/products', methods=['POST'])
@jwt_required()
def create_product():
    try:
        product_create_request = product_request_schema.load(request.json)
        product = Product.create(**product_create_request)

        return product_response_schema.dump(product), 201
    except ValidationError as e:
        raise HttpError.bad_request(message='Validation error', details=e.messages)


@blueprint.route('/api/products', methods=['GET'])
def find_all_products():
    products = Product.query.all()
    products = products_response_schema.dump(products)

    return jsonify(products)


@blueprint.route('/api/products/<int:product_id>', methods=['GET'])
def find_product_by_id(product_id):
    product = Product.query.get(product_id)

    if product is None:
        raise HttpError.not_found('product_not_found')

    return product_response_schema.dump(product)


@blueprint.route('/api/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    try:
        product_update_request = product_request_schema.load(request.json)
        
        product = Product.query.get(product_id)

        if product is None:
            raise HttpError.not_found('Product not found')

        product.update(**product_update_request)

        return product_response_schema.dump(product)
    except ValidationError as e:
        raise HttpError.bad_request(message='Validation error', details=e.messages)


@blueprint.route('/api/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    product = Product.query.get(product_id)
    product.delete()

    return jsonify(), 204
