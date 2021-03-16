"""create users table

Revision ID: 323ce8b0b529
Revises: a5a26660443d
Create Date: 2021-03-16 09:42:30.371776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '323ce8b0b529'
down_revision = 'a5a26660443d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(255), nullable=False, unique=True),
        sa.Column('password', sa.String(255), nullable=False)
    )


def downgrade():
    op.drop_table('users')
