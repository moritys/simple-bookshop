"""add desc field

Revision ID: 8a412a356641
Revises: 5263ad7a2e8e
Create Date: 2024-10-08 15:19:18.869461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a412a356641'
down_revision = '5263ad7a2e8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'description')
    # ### end Alembic commands ###