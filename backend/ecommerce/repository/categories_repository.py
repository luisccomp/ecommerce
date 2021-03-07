from ecommerce.database import db
from ecommerce.models.categories import Category


def save(category: Category) -> Category:
    db.session.add(category)
    db.session.commit()

    return category


def find_all() -> list[Category]:
    return Category.query.all()


def find_by_pk(pk) -> Category:
    return Category.query.get(pk)


def delete(category: Category):
    db.session.delete(category)
    db.session.commit()
