"""create employee table

Revision ID: d9ab1823ba8e
Revises: c1f658da483f
Create Date: 2025-03-09 11:27:32.032145

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9ab1823ba8e'
down_revision: Union[str, None] = 'c1f658da483f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the employee table, which depends on department
    op.create_table(
        'employee',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('birthday', sa.Date, nullable=False),
        sa.Column('department_id', sa.Integer, sa.ForeignKey('department.id', ondelete="SET NULL"), nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now())
    )

def downgrade() -> None:
    op.drop_table('employee')
