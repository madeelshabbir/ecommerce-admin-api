"""Create InventorySnaps

Revision ID: 0706dd527627
Revises: c8d7b5cd6fdd
Create Date: 2023-10-02 16:47:56.712646

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision: str = '0706dd527627'
down_revision: Union[str, None] = 'c8d7b5cd6fdd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
  op.create_table(
    'inventory_snaps',
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column('quantity', sa.Integer),
    sa.Column('created_at', sa.DateTime, default=sa.func.current_timestamp()),
    sa.Column('inventory_id', sa.Integer, sa.ForeignKey('inventories.id'))
  )

def downgrade() -> None:
  op.drop_table('inventory_snaps')
