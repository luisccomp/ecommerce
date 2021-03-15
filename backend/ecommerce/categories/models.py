from datetime import datetime
from ecommerce.database import Model, Column, db


class Category(Model):

    __tablename__ = 'categories'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(50), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(db.DateTime, nullable=True, default=None)
