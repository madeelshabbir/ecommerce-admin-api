"""Create Sales

Revision ID: 415ee1b6347c
Revises: 764559176816
Create Date: 2023-10-01 14:26:30.300255

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision: str = '415ee1b6347c'
down_revision: Union[str, None] = '764559176816'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  op.create_table(
    'sales',
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column('quantity', sa.Integer),
    sa.Column('created_at', sa.DateTime, default=sa.func.current_timestamp()),
    sa.Column('product_id', sa.Integer, sa.ForeignKey('products.id'))
  )

def downgrade() -> None:
  op.drop_table('sales')
