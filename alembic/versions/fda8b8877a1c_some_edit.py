"""some edit

Revision ID: fda8b8877a1c
Revises: 8ca62de4fa26
Create Date: 2024-12-13 01:42:02.116992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fda8b8877a1c'
down_revision: Union[str, None] = '8ca62de4fa26'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('products_user_id_fkey', 'products', type_='foreignkey')
    op.create_foreign_key(None, 'products', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.alter_column('users_diary', 'count',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=True)
    op.drop_constraint('users_diary_product_id_fkey', 'users_diary', type_='foreignkey')
    op.drop_constraint('users_diary_user_id_fkey', 'users_diary', type_='foreignkey')
    op.create_foreign_key(None, 'users_diary', 'products', ['product_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'users_diary', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users_diary', type_='foreignkey')
    op.drop_constraint(None, 'users_diary', type_='foreignkey')
    op.create_foreign_key('users_diary_user_id_fkey', 'users_diary', 'users', ['user_id'], ['id'])
    op.create_foreign_key('users_diary_product_id_fkey', 'users_diary', 'products', ['product_id'], ['id'])
    op.alter_column('users_diary', 'count',
               existing_type=sa.Integer(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.create_foreign_key('products_user_id_fkey', 'products', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###