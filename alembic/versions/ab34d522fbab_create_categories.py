"""Create Categories

Revision ID: ab34d522fbab
Revises:
Create Date: 2023-10-01 14:07:58.466762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'ab34d522fbab'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
  op.create_table(
    'categories',
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column('name', sa.String(255), unique=True, index=True)
  )

def downgrade() -> None:
  op.drop_table('categories')
