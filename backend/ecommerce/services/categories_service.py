from ecommerce.models.categories import Category
from ecommerce.repository import categories_repository
from ecommerce.exceptions import NotFoundException


def create_category(category_create_request):
    category = Category.from_json(category_create_request)
    category = categories_repository.save(category)

    return category.to_response()


def find_all_categories():
    categories = categories_repository.find_all()

    return list(map(lambda category: category.to_response(), categories))


def find_category_by_id(pk: int):
    category = categories_repository.find_by_pk(pk)

    if not category: 
        raise NotFoundException(message='Category not found')

    return category.to_response()


def update_category(pk: int, category_update_request):
    category = categories_repository.find_by_pk(pk)

    if not category:
        raise NotFoundException(message='Category not found')

    category.name = category_update_request.get('name')
    category = categories_repository.save(category)

    return category.to_response()


def delete_category(pk: int):
    category = categories_repository.find_by_pk(pk)

    if not category:
        raise NotFoundException(message='Category not found')

    categories_repository.delete(category)
