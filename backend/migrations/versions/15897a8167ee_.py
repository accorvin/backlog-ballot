"""empty message

Revision ID: 15897a8167ee
Revises: e65ca0dbec70
Create Date: 2018-06-25 19:20:00.725563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15897a8167ee'
down_revision = 'e65ca0dbec70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issue', sa.Column('jira_key', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('issue', 'jira_key')
    # ### end Alembic commands ###
