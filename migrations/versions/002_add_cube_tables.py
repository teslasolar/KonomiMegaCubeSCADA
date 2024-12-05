"""Add cube tables

Revision ID: 002
Revises: 001
Create Date: 2024-12-04 06:50:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None

def upgrade():
    # Create konomi_cubes table
    op.create_table('konomi_cubes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('cube_id', sa.String(length=50), nullable=False),
        sa.Column('cube_type', sa.String(length=50), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('metadata', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('parent_id', sa.Integer(), nullable=True),
        sa.Column('validation_rules', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('isolation_level', sa.String(length=20), nullable=True),
        sa.ForeignKeyConstraint(['parent_id'], ['konomi_cubes.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('cube_id')
    )

    # Create snitch_cubes table
    op.create_table('snitch_cubes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('violation_threshold', sa.Integer(), nullable=True),
        sa.Column('monitoring_rules', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(['id'], ['konomi_cubes.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Create dependency_cubes table
    op.create_table('dependency_cubes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('dependency_rules', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('max_depth', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['id'], ['konomi_cubes.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Create ktool_cubes table
    op.create_table('ktool_cubes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('tool_configs', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(['id'], ['konomi_cubes.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Create scada_cubes table
    op.create_table('scada_cubes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('scada_type', sa.String(length=50), nullable=False),
        sa.Column('configuration', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(['id'], ['konomi_cubes.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create sop_emergency_cubes table
    op.create_table('sop_emergency_cubes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('change_validation_rules', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('priority_thresholds', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('approval_workflow', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(['id'], ['konomi_cubes.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('sop_emergency_cubes')
    op.drop_table('scada_cubes')
    op.drop_table('ktool_cubes')
    op.drop_table('dependency_cubes')
    op.drop_table('snitch_cubes')
    op.drop_table('konomi_cubes')
