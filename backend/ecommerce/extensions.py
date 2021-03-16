from flask_sqlalchemy import SQLAlchemy, Model
from flask_bcrypt import Bcrypt
from flask_jwt import JWT


class CRUDMixin(Model):
    """Base Model class with basic CRUD (create, read, update, delete) operations implemented on itself. This makes a
    model class behave like an active record.
    """

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it on database"""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record"""
        for attr, value in kwargs.items():
            setattr(self, attr, value)

        return self.save(commit)

    def save(self, commit=True):
        """Save a record on database."""
        db.session.add(self)

        if commit:
            db.session.commit()

        return self

    def delete(self, commit=True):
        """Remove the record from database"""
        db.session.delete(self)

        if commit:
            db.session.commit()


db = SQLAlchemy(model_class=CRUDMixin)
bcrypt = Bcrypt()

jwt = JWT()
