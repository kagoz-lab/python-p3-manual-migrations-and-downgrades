"""Create table students

Revision ID: 791279dd0760
Revises: 
Create Date: 2023-10-10 10:00:00
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '791279dd0760'
down_revision = None  # Update this if there is a previous revision
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'students',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), index=True),
        sa.Column('email', sa.String(55)),
        sa.Column('grade', sa.Integer()),
        sa.Column('birthday', sa.DateTime()),
        sa.Column('enrolled_date', sa.DateTime(), default=sa.func.now())
    )

def downgrade() -> None:
    op.drop_table('students')
