from datetime import datetime

from marshmallow import Schema, fields, validate
from ecommerce.database import Model, Column, db


class CategoryRequestSchema(Schema):

    name = fields.String(required=True, validate=validate.Length(max=50), allow_none=False)


class Category(Model):

    __tablename__ = 'categories'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(50), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(db.DateTime, nullable=True, default=datetime.utcnow())
    # products = db.relationship('Product', backref='person', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    @classmethod
    def from_json(cls, json):
        return cls(name=json['name'])

    def to_response(self):
        return {
            'id': self.id,
            'name': self.name
        }
