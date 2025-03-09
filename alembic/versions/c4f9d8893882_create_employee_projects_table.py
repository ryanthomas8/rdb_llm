"""create employee_projects table

Revision ID: c4f9d8893882
Revises: eab101d10af0
Create Date: 2025-03-09 11:28:11.321497

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c4f9d8893882"
down_revision: Union[str, None] = "eab101d10af0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the employee_projects table (many-to-many relationship)
    op.create_table(
        "employee_projects",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "employee_id", sa.Integer, sa.ForeignKey("employee.id", ondelete="CASCADE")
        ),
        sa.Column(
            "project_id", sa.Integer, sa.ForeignKey("project.id", ondelete="CASCADE")
        ),
        sa.Column("role", sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("employee_projects")
