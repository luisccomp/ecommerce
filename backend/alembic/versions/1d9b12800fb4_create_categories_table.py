"""create categories table

Revision ID: 1d9b12800fb4
Revises: 
Create Date: 2021-03-11 18:33:47.814459

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d9b12800fb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """UPGRADE: é a atualização do nosso schema de banco de dados: create table, add column, etc."""
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False, default=datetime.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=True, default=None)
    )


def downgrade():
    """DOWNGRADE: é o contrário --> desfazer as alterações feitas no schema"""
    op.drop_table("categories")
