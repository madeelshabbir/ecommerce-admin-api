"""Rename inventories.stock_quantity to inventories.quantity

Revision ID: c8d7b5cd6fdd
Revises: 415ee1b6347c
Create Date: 2023-10-01 21:32:21.858578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision: str = 'c8d7b5cd6fdd'
down_revision: Union[str, None] = '415ee1b6347c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
  op.alter_column('inventories', 'stock_quantity', existing_type=sa.Integer, new_column_name='quantity')

def downgrade() -> None:
  op.alter_column('inventories', 'quantity', existing_type=sa.Integer, new_column_name='stock_quantity')
