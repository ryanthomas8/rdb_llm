"""create salary table

Revision ID: 1fc90f347ea1
Revises: d9ab1823ba8e
Create Date: 2025-03-09 11:27:46.220790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1fc90f347ea1'
down_revision: Union[str, None] = 'd9ab1823ba8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the salary table, which depends on employee
    op.create_table(
        'salary',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('employee_id', sa.Integer, sa.ForeignKey('employee.id', ondelete="CASCADE")),
        sa.Column('salary', sa.DECIMAL(10, 2), nullable=False),
        sa.Column('start_date', sa.Date, nullable=False),
        sa.Column('end_date', sa.Date, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('salary')
