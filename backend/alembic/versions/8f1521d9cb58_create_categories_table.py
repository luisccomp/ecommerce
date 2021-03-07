"""create categories table

Revision ID: 8f1521d9cb58
Revises: 
Create Date: 2021-03-06 20:21:50.450511

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f1521d9cb58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.utcnow()),
        sa.Column('updated_at', sa.DateTime, nullable=True, default=datetime.utcnow())
    )


def downgrade():
    op.drop_table('categories')
