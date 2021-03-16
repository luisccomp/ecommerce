from datetime import datetime
from ecommerce.database import Model, Column, db


class Product(Model):

    __tablename__ = 'products'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(50), nullable=False)
    description = Column(db.String(250), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(db.DateTime, nullable=True, default=None)
    category_id = Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('products', lazy=True))

    def __repr__(self):
        return '<Product %r>' % self.name
