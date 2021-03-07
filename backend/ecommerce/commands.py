from flask.cli import with_appcontext

import click

from .extensions import db


@click.command(name='init-db', help='Init database and create all tables')
@with_appcontext
def init_db():
    db.create_all()
