"""test

Revision ID: 2a7778bcde76
Revises: b7437e092873
Create Date: 2022-05-08 20:50:08.557134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2a7778bcde76"
down_revision = "b7437e092873"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("bookshelves", sa.Column("test", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("bookshelves", "test")
    # ### end Alembic commands ###
