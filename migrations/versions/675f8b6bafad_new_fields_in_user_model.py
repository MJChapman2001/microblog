"""new fields in user model

Revision ID: 675f8b6bafad
Revises: 167d999d089a
Create Date: 2022-02-08 21:47:45.045147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '675f8b6bafad'
down_revision = '167d999d089a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
