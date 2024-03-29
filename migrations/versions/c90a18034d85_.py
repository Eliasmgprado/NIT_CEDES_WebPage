"""empty message

Revision ID: c90a18034d85
Revises: 8a32dbe0f6ac
Create Date: 2018-03-26 08:36:30.283102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c90a18034d85'
down_revision = '8a32dbe0f6ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('file_dir', sa.String(length=512), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'file_dir')
    # ### end Alembic commands ###
