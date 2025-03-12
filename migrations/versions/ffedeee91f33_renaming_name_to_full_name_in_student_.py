"""Renaming name to full_name in Student model

Revision ID: ffedeee91f33
Revises: 
Create Date: 2023-10-10 10:00:00
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ffedeee91f33'
down_revision = None  # Update this if there is a previous revision
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='full_name')

def downgrade() -> None:
    op.alter_column('students', 'full_name', new_column_name='name')
