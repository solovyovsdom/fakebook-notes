"""empty message

Revision ID: 9881f4aa256e
Revises: f960202465dd
Create Date: 2021-11-22 21:07:28.639561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9881f4aa256e'
down_revision = 'f960202465dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###