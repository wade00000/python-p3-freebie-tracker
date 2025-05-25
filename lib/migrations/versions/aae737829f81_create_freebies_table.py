"""Create freebies table

Revision ID: aae737829f81
Revises: 5f72c58bf48c
Create Date: 2025-05-25 21:53:21.720728

"""
from alembic import op
import sqlalchemy as sa



revision = 'aae737829f81'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id')),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'))
    )



def downgrade():
    op.drop_table('freebies')

