"""empty message

Revision ID: d32767d5ea90
Revises: eace192c486c
Create Date: 2018-03-22 11:29:22.371158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd32767d5ea90'
down_revision = 'eace192c486c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('role', sa.String(length=128), nullable=True),
    sa.Column('intro', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_name'), 'team', ['name'], unique=True)
    op.drop_index('ix_news_title', table_name='news')
    op.create_index(op.f('ix_news_title'), 'news', ['title'], unique=False)
    op.drop_index('ix_publications_title', table_name='publications')
    op.create_index(op.f('ix_publications_title'), 'publications', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_publications_title'), table_name='publications')
    op.create_index('ix_publications_title', 'publications', ['title'], unique=1)
    op.drop_index(op.f('ix_news_title'), table_name='news')
    op.create_index('ix_news_title', 'news', ['title'], unique=1)
    op.drop_index(op.f('ix_team_name'), table_name='team')
    op.drop_table('team')
    # ### end Alembic commands ###
