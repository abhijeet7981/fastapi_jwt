# """create address_id to products

# Revision ID: 73b769bf7cb7
# Revises: e97706776c89
# Create Date: 2023-04-24 13:23:40.265431

# """
# from alembic import op
# import sqlalchemy as sa


# # revision identifiers, used by Alembic.
# revision = '73b769bf7cb7'
# down_revision = 'e97706776c89'
# branch_labels = None
# depends_on = None


# def upgrade() -> None:
#     op.add_column('products',sa.Column('address_id',sa.Integer(),nullable=True))
#     op.create_foreign_key('address_products_fk',source_table='products',referent_table='address',
#                           local_cols=['address_id'],remote_cols=['id'],ondelete="CASCADE")


# def downgrade() -> None:
#     op.drop_constraints('address_product_fk',table_name='products')
#     op.drop_column('products','address_id')
