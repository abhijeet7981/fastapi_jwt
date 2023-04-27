"""create phone number for products col

Revision ID: 9df9c99e4501
Revises: 
Create Date: 2023-04-24 12:53:33.111394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9df9c99e4501'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('products',sa.Column('phone_number',sa.Integer(),nullable=True))
    


def downgrade():
    op.drop_column('products','phone_number')
