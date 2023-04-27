"""create account table

Revision ID: b6ecbb4dfe84
Revises: 73b769bf7cb7
Create Date: 2023-04-26 15:29:32.287463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6ecbb4dfe84'
down_revision = '73b769bf7cb7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('sellers',sa.Column('passcode',sa.Integer(),nullable=True))


def downgrade() -> None:
    pass
