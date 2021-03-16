from ecommerce.database import Model, Column, db
from ecommerce.extensions import bcrypt, jwt
from ecommerce.exceptions import HttpError


class User(Model):

    __tablename__ = "users"

    id = Column(db.Integer, primary_key=True)
    email = Column(db.String(255), nullable=False, unique=True)
    password = Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


@jwt.authentication_handler
def authenticate(username, password):
    user = User.query.filter_by(email=username).first()

    if user is None or not bcrypt.check_password_hash(user.password, password):
        raise HttpError.unauthorized(message='Username or password might be incorrect')

    return user


@jwt.identity_handler
def identity(payload):
    user_id = payload['identity']

    user = User.query.get(user_id)

    if user is None:
        raise HttpError.unauthorized()

    return user
