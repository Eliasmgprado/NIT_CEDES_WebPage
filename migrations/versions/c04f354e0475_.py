"""empty message

Revision ID: c04f354e0475
Revises: 
Create Date: 2018-03-24 10:14:27.745974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c04f354e0475'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('abrev', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category')
    )
    op.create_table('publication_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('role', sa.String(length=128), nullable=True),
    sa.Column('intro', sa.Text(), nullable=True),
    sa.Column('foto', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_name'), 'team', ['name'], unique=True)
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('intro', sa.String(length=512), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['news_categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_news_date'), 'news', ['date'], unique=False)
    op.create_index(op.f('ix_news_title'), 'news', ['title'], unique=False)
    op.create_table('publications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('abstract', sa.Text(), nullable=True),
    sa.Column('file_dir', sa.String(length=256), nullable=True),
    sa.Column('img_dir', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['publication_categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_publications_date'), 'publications', ['date'], unique=False)
    op.create_index(op.f('ix_publications_title'), 'publications', ['title'], unique=False)
    op.create_table('pub_authors',
    sa.Column('pub_id', sa.Integer(), nullable=True),
    sa.Column('auth_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['auth_id'], ['authors.id'], ),
    sa.ForeignKeyConstraint(['pub_id'], ['publications.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pub_authors')
    op.drop_index(op.f('ix_publications_title'), table_name='publications')
    op.drop_index(op.f('ix_publications_date'), table_name='publications')
    op.drop_table('publications')
    op.drop_index(op.f('ix_news_title'), table_name='news')
    op.drop_index(op.f('ix_news_date'), table_name='news')
    op.drop_table('news')
    op.drop_index(op.f('ix_team_name'), table_name='team')
    op.drop_table('team')
    op.drop_table('publication_categories')
    op.drop_table('news_categories')
    op.drop_table('authors')
    # ### end Alembic commands ###