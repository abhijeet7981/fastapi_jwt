# """create address table

# Revision ID: e97706776c89
# Revises: 9df9c99e4501
# Create Date: 2023-04-24 13:14:58.170808

# """
# from alembic import op
# import sqlalchemy as sa


# # revision identifiers, used by Alembic.
# revision = 'e97706776c89'
# down_revision = '9df9c99e4501'
# branch_labels = None
# depends_on = None


# def upgrade() -> None:
#     op.create_table('sellers',
                    
#                     sa.Column('passcode',sa.String(),nullable=False)
                    
#                     )


# def downgrade() -> None:
#     op.drop_table('address')