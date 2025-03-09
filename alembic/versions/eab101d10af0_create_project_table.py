"""create project table

Revision ID: eab101d10af0
Revises: 1fc90f347ea1
Create Date: 2025-03-09 11:27:57.811023

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "eab101d10af0"
down_revision: Union[str, None] = "1fc90f347ea1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the project table (no dependencies)
    op.create_table(
        "project",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("budget", sa.DECIMAL(12, 2), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("project")
