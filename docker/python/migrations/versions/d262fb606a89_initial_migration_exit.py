"""Initial migration.exit

Revision ID: d262fb606a89
Revises: f461601ff148
Create Date: 2024-05-28 02:43:06.851229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd262fb606a89'
down_revision = 'f461601ff148'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('manage_user', sa.Column('password', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('manage_user', 'password')
    # ### end Alembic commands ###