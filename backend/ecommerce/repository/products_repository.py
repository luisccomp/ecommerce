from ecommerce.database import db


def add(product):
    db.session.add(product)
    db.session.commit()

    return product
