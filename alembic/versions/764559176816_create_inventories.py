"""Create Inventories

Revision ID: 764559176816
Revises: fa10284e939b
Create Date: 2023-10-01 14:22:34.402669

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision: str = '764559176816'
down_revision: Union[str, None] = 'fa10284e939b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  op.create_table(
    'inventories',
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column('stock_quantity', sa.Integer),
    sa.Column('updated_at', sa.DateTime),
    sa.Column('product_id', sa.Integer, sa.ForeignKey('products.id'))
  )

def downgrade() -> None:
  op.drop_table('inventories')
