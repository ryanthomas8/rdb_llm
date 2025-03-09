"""create all tables

Revision ID: c1f658da483f
Revises:
Create Date: 2025-03-07 11:33:10.453448

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "c1f658da483f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create the department table first
    op.create_table(
        "department",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False, unique=True),
    )


def downgrade():
    op.drop_table("department")
