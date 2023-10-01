"""Create Products

Revision ID: fa10284e939b
Revises: ab34d522fbab
Create Date: 2023-10-01 14:16:34.924735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision: str = 'fa10284e939b'
down_revision: Union[str, None] = 'ab34d522fbab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  op.create_table(
    'products',
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column('title', sa.String(255), index=True),
    sa.Column('description', sa.String(1000)),
    sa.Column('price', sa.Float),
    sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
    sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id'))
  )

def downgrade() -> None:
  op.drop_table('products')
