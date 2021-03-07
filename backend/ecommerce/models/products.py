from ecommerce.database import Model, Column, db


class Product(Model):

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(50), nullable=False)
    description = Column(db.String(255), nullable=False)
    category_id = Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    @classmethod
    def from_json(cls, json, category_id):
        return cls(
            name=json['name'], 
            description=json['description'], 
            category_id=category_id
        )

    def to_response(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
