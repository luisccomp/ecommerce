from unittest import TestCase, mock
from ecommerce.services import categories_service
from ecommerce.models.categories import Category
from ecommerce.exceptions import NotFoundException


class CategoriesServiceTest(TestCase):

    def test_create_category(self):
        """Should create a category and store it on database."""
        # Mocking repository behavior of categories services in order to simulate database operations
        category_create_request = {'name': 'Books'}

        categories_service.categories_repository.save = mock.Mock()
        categories_service.categories_repository.save.return_value = Category(
            id=1,
            name=category_create_request.get('name')
        )

        category = categories_service.create_category(category_create_request)

        assert category.get('id') == 1
        assert category.get('name') == category_create_request.get('name')

    def test_find_all_categories(self):
        """Should return all categories stored on database."""
        categories_service.categories_repository.find_all = mock.Mock()
        categories_service.categories_repository.find_all.return_value = [
            Category(id=1, name='Games'),
            Category(id=2, name='Informatics')
        ]

        categories = categories_service.find_all_categories()
        
        assert len(categories) == 2

    def test_find_category_by_pk(self):
        """Should find a category given it's primary key."""
        category_id = 1

        categories_service.categories_repository.find_by_pk = mock.Mock()
        categories_service.categories_repository.find_by_pk.return_value = Category(
            id = category_id,
            name = 'Games'
        )

        category = categories_service.find_category_by_id(category_id)

        assert category.get('id') == category_id
        assert category.get('name') == 'Games'

    def test_find_category_by_pk_not_found(self):
        """Should raise an exception when try to find a category that doesn't exists"""
        category_id = 1

        categories_service.categories_repository.find_by_pk = mock.Mock()
        categories_service.categories_repository.find_by_pk.return_value = None

        try:
            categories_service.find_category_by_id(category_id)
            assert False
        except Exception as e:
            assert isinstance(e, NotFoundException)
            assert e.status == 404
            assert e.message == 'Category not found'

    def test_update_category(self):
        """Should update a category."""
        category_id = 1
        category_update_request = {'name': 'Consoles'}

        categories_service.categories_repository.find_by_pk = mock.Mock()
        categories_service.categories_repository.find_by_pk.return_value = Category(
            id = category_id,
            name = '' # The name here doesn't matter since it's going to be updated
        )

        categories_service.categories_repository.save = mock.Mock()
        categories_service.categories_repository.save.return_value = Category(
            id = category_id,
            name = category_update_request.get('name')
        )

        category = categories_service.update_category(category_id, category_update_request)

        assert category.get('id') == category_id
        assert category.get('name') == category_update_request.get('name')

    def test_update_category_not_found(self):
        """Should raise an error when try to update a category that doesn't exists."""
        category_id = 1
        category_update_request = {'name': 'Consoles'}

        categories_service.categories_repository.find_by_pk = mock.Mock()
        categories_service.categories_repository.find_by_pk.return_value = None

        try:
            categories_service.update_category(category_id, category_update_request)
            assert False
        except Exception as e:
            assert isinstance(e, NotFoundException)
            assert e.status == 404
            assert e.message == 'Category not found'

    def test_delete_category(self):
        """Should delete a category from database."""
        category_id = 1

        category = Category(
            id = category_id,
            name = 'Games'
        )

        categories_service.categories_repository.find_by_pk = mock.Mock()
        categories_service.categories_repository.find_by_pk.return_value = category

        categories_service.categories_repository.delete = mock.Mock()

        categories_service.delete_category(category_id)

        categories_service.categories_repository.delete.assert_called_once_with(category)

    def test_delete_category_not_found(self):
        category_id = 1

        categories_service.categories_repository.find_by_pk = mock.Mock()
        categories_service.categories_repository.find_by_pk.return_value = None

        try:
            categories_service.delete_category(category_id)
        except Exception as e:
            assert isinstance(e, NotFoundException)
            assert e.status == 404
            assert e.message == 'Category not found'
