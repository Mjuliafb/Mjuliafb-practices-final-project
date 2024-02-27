"""empty message

Revision ID: 334499e6e697
Revises: 
Create Date: 2024-02-27 18:28:12.116111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '334499e6e697'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('img', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gift',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('link', sa.String(length=120), nullable=False),
    sa.Column('status', sa.String(length=80), nullable=False),
    sa.Column('img', sa.String(length=80), nullable=False),
    sa.Column('list_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['list.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link'),
    sa.UniqueConstraint('list_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gift')
    op.drop_table('list')
    op.drop_table('user')
    # ### end Alembic commands ###