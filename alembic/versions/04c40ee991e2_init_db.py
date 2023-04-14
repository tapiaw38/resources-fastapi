"""init_db

Revision ID: 04c40ee991e2
Revises:
Create Date: 2023-04-08 16:51:00.821201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04c40ee991e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'employee_type',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column(
            'name',
            sa.String(150),
            unique=True,
            index=True,
            nullable=False
        ),
        sa.Column('description', sa.String(150), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP, server_default='now()'),
        sa.Column('updated_at', sa.TIMESTAMP, server_default='now()'),
    )
    op.create_table(
        'workplace',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('code', sa.String(150), unique=True, nullable=False),
        sa.Column('address', sa.String(150), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP, server_default='now()'),
        sa.Column('updated_at', sa.TIMESTAMP, server_default='now()'),
    )
    op.create_table(
        'employee',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('file_code', sa.String(150), unique=True),
        sa.Column('agent_number', sa.String(150), unique=True),
        sa.Column('first_name', sa.String(150), nullable=False),
        sa.Column('last_name', sa.String(150), server_default=''),
        sa.Column(
            'document_number',
            sa.String(150),
            unique=True,
            nullable=True
        ),
        sa.Column('birth_date', sa.Date, nullable=True),
        sa.Column('date_admission', sa.Date, nullable=True),
        sa.Column('phone', sa.String(150), server_default=''),
        sa.Column('address', sa.String(150), server_default=''),
        sa.Column('picture', sa.String(256), server_default=''),
        sa.Column('salary', sa.Numeric(10, 2), server_default='0'),
        sa.Column('category', sa.Integer, server_default='10'),
        sa.Column('status', sa.Integer, server_default='1'),
        sa.Column('work_number', sa.String(150), server_default=''),
        sa.Column(
            'employee_type',
            sa.Integer,
            sa.ForeignKey('employee_type.id', ondelete='CASCADE'),
            nullable=True
        ),
        sa.Column(
            'workplace',
            sa.Integer,
            sa.ForeignKey('workplace.id', ondelete='CASCADE'),
            nullable=True
        ),
        sa.Column('created_at', sa.TIMESTAMP, server_default='now()'),
        sa.Column('updated_at', sa.TIMESTAMP, server_default='now()'),
        sa.ForeignKeyConstraint(
            ['employee_type'],
            ['employee_type.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['workplace'],
            ['workplace.id'],
            ondelete='CASCADE'
        ),
    )


def downgrade() -> None:
    op.drop_table('employees')
    op.drop_table('employee_type')
    op.drop_table('workplace')
