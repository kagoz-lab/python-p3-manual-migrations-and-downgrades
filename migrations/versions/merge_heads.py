"""Merge heads

Revision ID: merge_heads
Revises: 791279dd0760, ffedeee91f33
Create Date: 2023-10-10 10:00:00
"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'merge_heads'
down_revision = ('791279dd0760', 'ffedeee91f33')  # Specify both head revisions
branch_labels = None
depends_on = None

def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
