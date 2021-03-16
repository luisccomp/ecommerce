"""create products table

Revision ID: a5a26660443d
Revises: 1d9b12800fb4
Create Date: 2021-03-16 08:19:26.920900

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5a26660443d'
down_revision = '1d9b12800fb4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.utcnow()),
        sa.Column('updated_at', sa.DateTime, nullable=True, default=None),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id'), nullable=False)
    )


def downgrade():
    op.drop_table('products')
