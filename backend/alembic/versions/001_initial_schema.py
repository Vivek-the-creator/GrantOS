"""001_initial_schema

Revision ID: 001_initial_schema
Revises: 
Create Date: 2026-09-20 19:30:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '001_initial_schema'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Users
    op.create_table(
        'users',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('full_name', sa.String(length=255), nullable=False),
        sa.Column('role', sa.Enum('GOV_ADMIN', 'BENEFICIARY_STUDENT', 'NGO_ORG', 'MERCHANT', 'AUDITOR', name='user_role_enum'), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='1'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)

    # 2. Grant Programs
    op.create_table(
        'grant_programs',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('code', sa.String(length=64), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('department', sa.String(length=128), nullable=False),
        sa.Column('total_budget', sa.Numeric(precision=14, scale=2), nullable=False),
        sa.Column('currency', sa.String(length=8), nullable=False, server_default='INR'),
        sa.Column('status', sa.Enum('DRAFT', 'ACTIVE', 'PAUSED', 'COMPLETED', 'ARCHIVED', name='grant_program_status_enum'), nullable=False),
        sa.Column('rules_policy_json', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_grant_programs_code'), 'grant_programs', ['code'], unique=True)

    # 3. Grants
    op.create_table(
        'grants',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('program_id', sa.UUID(), nullable=False),
        sa.Column('beneficiary_id', sa.UUID(), nullable=False),
        sa.Column('grant_number', sa.String(length=64), nullable=False),
        sa.Column('allocated_amount', sa.Numeric(precision=14, scale=2), nullable=False),
        sa.Column('spent_amount', sa.Numeric(precision=14, scale=2), nullable=False, server_default='0.00'),
        sa.Column('currency', sa.String(length=8), nullable=False, server_default='INR'),
        sa.Column('status', sa.Enum('CREATED', 'APPROVED', 'ISSUED', 'RELEASED', 'SPENDING_ACTIVE', 'SUSPENDED', 'CLOSED', 'REVOKED', name='grant_status_enum'), nullable=False),
        sa.Column('valid_from', sa.DateTime(timezone=True), nullable=True),
        sa.Column('valid_until', sa.DateTime(timezone=True), nullable=True),
        sa.Column('blockchain_grant_hash', sa.String(length=128), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['beneficiary_id'], ['users.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['program_id'], ['grant_programs.id'], ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_grants_grant_number'), 'grants', ['grant_number'], unique=True)

    # 4. Scholarship Applications
    op.create_table(
        'scholarship_applications',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('program_id', sa.UUID(), nullable=False),
        sa.Column('applicant_id', sa.UUID(), nullable=False),
        sa.Column('application_number', sa.String(length=64), nullable=False),
        sa.Column('status', sa.Enum('SUBMITTED', 'UNDER_REVIEW', 'VERIFIED', 'APPROVED', 'REJECTED', name='application_status_enum'), nullable=False),
        sa.Column('submitted_data_json', sa.JSON(), nullable=True),
        sa.Column('ai_risk_score', sa.Numeric(precision=5, scale=2), nullable=True),
        sa.Column('reviewed_by_id', sa.UUID(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['applicant_id'], ['users.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['program_id'], ['grant_programs.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['reviewed_by_id'], ['users.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_scholarship_applications_application_number'), 'scholarship_applications', ['application_number'], unique=True)

    # 5. Application Documents
    op.create_table(
        'application_documents',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('application_id', sa.UUID(), nullable=False),
        sa.Column('document_type', sa.String(length=64), nullable=False),
        sa.Column('file_name', sa.String(length=255), nullable=False),
        sa.Column('storage_path', sa.String(length=512), nullable=False),
        sa.Column('sha256_hash', sa.String(length=64), nullable=False),
        sa.Column('verification_status', sa.Enum('PENDING', 'VERIFIED', 'FLAGGED', 'REJECTED', name='verification_status_enum'), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['application_id'], ['scholarship_applications.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # 6. Merchants
    op.create_table(
        'merchants',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.UUID(), nullable=True),
        sa.Column('business_name', sa.String(length=255), nullable=False),
        sa.Column('merchant_code', sa.String(length=64), nullable=False),
        sa.Column('mcc', sa.String(length=16), nullable=False),
        sa.Column('category', sa.String(length=64), nullable=False),
        sa.Column('is_verified', sa.Boolean(), nullable=False, server_default='1'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_merchants_category'), 'merchants', ['category'], unique=False)
    op.create_index(op.f('ix_merchants_mcc'), 'merchants', ['mcc'], unique=False)
    op.create_index(op.f('ix_merchants_merchant_code'), 'merchants', ['merchant_code'], unique=True)

    # 7. Grant Transactions
    op.create_table(
        'grant_transactions',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('grant_id', sa.UUID(), nullable=False),
        sa.Column('beneficiary_id', sa.UUID(), nullable=False),
        sa.Column('merchant_id', sa.UUID(), nullable=False),
        sa.Column('amount', sa.Numeric(precision=14, scale=2), nullable=False),
        sa.Column('currency', sa.String(length=8), nullable=False, server_default='INR'),
        sa.Column('merchant_category', sa.String(length=64), nullable=False),
        sa.Column('decision', sa.Enum('APPROVED', 'BLOCKED', name='transaction_decision_enum'), nullable=False),
        sa.Column('decision_reason', sa.Text(), nullable=False),
        sa.Column('payment_reference', sa.String(length=128), nullable=True),
        sa.Column('blockchain_tx_hash', sa.String(length=128), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['beneficiary_id'], ['users.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['grant_id'], ['grants.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['merchant_id'], ['merchants.id'], ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('id')
    )

    # 8. Grant Milestones
    op.create_table(
        'grant_milestones',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('grant_id', sa.UUID(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('milestone_index', sa.Integer(), nullable=False),
        sa.Column('target_amount', sa.Numeric(precision=14, scale=2), nullable=False),
        sa.Column('status', sa.Enum('PENDING', 'IN_PROGRESS', 'SUBMITTED', 'VERIFIED', 'APPROVED', 'RELEASABLE', 'RELEASED', name='milestone_status_enum'), nullable=False),
        sa.Column('approved_by_id', sa.UUID(), nullable=True),
        sa.Column('tranche_release_ref', sa.String(length=128), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['approved_by_id'], ['users.id'], ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['grant_id'], ['grants.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # 9. Milestone Evidences
    op.create_table(
        'milestone_evidences',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('milestone_id', sa.UUID(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('file_name', sa.String(length=255), nullable=False),
        sa.Column('storage_path', sa.String(length=512), nullable=False),
        sa.Column('sha256_hash', sa.String(length=64), nullable=False),
        sa.Column('verification_status', sa.Enum('PENDING', 'VERIFIED', 'FLAGGED', 'REJECTED', name='evidence_verification_status_enum'), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['milestone_id'], ['grant_milestones.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # 10. Audit Events
    op.create_table(
        'audit_events',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('event_type', sa.Enum('GRANT_CREATED', 'GRANT_APPROVED', 'GRANT_ISSUED', 'FUNDS_RELEASED', 'SPENDING_REQUESTED', 'SPENDING_APPROVED', 'SPENDING_BLOCKED', 'MILESTONE_CREATED', 'EVIDENCE_SUBMITTED', 'MILESTONE_APPROVED', 'TRANCHE_RELEASED', 'GRANT_SUSPENDED', 'GRANT_REVOKED', 'GRANT_CLOSED', name='audit_event_type_enum'), nullable=False),
        sa.Column('actor_id', sa.UUID(), nullable=True),
        sa.Column('entity_type', sa.String(length=64), nullable=False),
        sa.Column('entity_id', sa.String(length=128), nullable=False),
        sa.Column('event_metadata', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['actor_id'], ['users.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_audit_events_created_at'), 'audit_events', ['created_at'], unique=False)
    op.create_index(op.f('ix_audit_events_entity_id'), 'audit_events', ['entity_id'], unique=False)
    op.create_index(op.f('ix_audit_events_entity_type'), 'audit_events', ['entity_type'], unique=False)
    op.create_index(op.f('ix_audit_events_event_type'), 'audit_events', ['event_type'], unique=False)


def downgrade() -> None:
    op.drop_table('audit_events')
    op.drop_table('milestone_evidences')
    op.drop_table('grant_milestones')
    op.drop_table('grant_transactions')
    op.drop_table('merchants')
    op.drop_table('application_documents')
    op.drop_table('scholarship_applications')
    op.drop_table('grants')
    op.drop_table('grant_programs')
    op.drop_table('users')
