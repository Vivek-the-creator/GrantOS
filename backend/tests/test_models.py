import pytest
from decimal import Decimal
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import (
    User,
    UserRole,
    GrantProgram,
    GrantProgramStatus,
    Grant,
    GrantStatus,
    ScholarshipApplication,
    ApplicationStatus,
    Merchant,
    GrantTransaction,
    TransactionDecision,
    GrantMilestone,
    MilestoneStatus,
    AuditEvent,
    AuditEventType,
)


@pytest.mark.asyncio
async def test_user_model_creation(db_session: AsyncSession):
    user = User(
        email="student001@university.edu",
        full_name="Alex Student",
        role=UserRole.BENEFICIARY_STUDENT,
    )
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)

    assert user.id is not None
    assert user.email == "student001@university.edu"
    assert user.role == UserRole.BENEFICIARY_STUDENT
    assert user.is_active is True


@pytest.mark.asyncio
async def test_grant_program_and_grant_relationship(db_session: AsyncSession):
    student = User(
        email="beneficiary@edu.in",
        full_name="Rajesh Kumar",
        role=UserRole.BENEFICIARY_STUDENT,
    )
    db_session.add(student)
    await db_session.commit()

    program = GrantProgram(
        title="National Higher Education Grant 2026",
        code="EDU-2026-NAT",
        department="Ministry of Education",
        total_budget=Decimal("50000000.00"),  # 5 Crore INR
        status=GrantProgramStatus.ACTIVE,
    )
    db_session.add(program)
    await db_session.commit()

    grant = Grant(
        program_id=program.id,
        beneficiary_id=student.id,
        grant_number="GRN-2026-EDU-8812",
        allocated_amount=Decimal("80000.00"),
        spent_amount=Decimal("0.00"),
        status=GrantStatus.SPENDING_ACTIVE,
    )
    db_session.add(grant)
    await db_session.commit()
    await db_session.refresh(grant)

    assert grant.allocated_amount == Decimal("80000.00")
    assert grant.remaining_balance == Decimal("80000.00")
    assert grant.program.code == "EDU-2026-NAT"
    assert grant.beneficiary.full_name == "Rajesh Kumar"


@pytest.mark.asyncio
async def test_merchant_and_transaction_flow_representation(db_session: AsyncSession):
    student = User(
        email="stu88@college.edu",
        full_name="Priya Sharma",
        role=UserRole.BENEFICIARY_STUDENT,
    )
    program = GrantProgram(
        title="Engineering Scholarship Scheme",
        code="ENG-SCH-2026",
        department="Technical Education Board",
        total_budget=Decimal("10000000.00"),
    )
    db_session.add_all([student, program])
    await db_session.commit()

    grant = Grant(
        program_id=program.id,
        beneficiary_id=student.id,
        grant_number="GRN-ENG-001",
        allocated_amount=Decimal("80000.00"),
        spent_amount=Decimal("45000.00"),
        status=GrantStatus.SPENDING_ACTIVE,
    )
    merchant = Merchant(
        business_name="ABC Engineering College",
        merchant_code="MER-COLLEGE-001",
        mcc="8220",
        category="EDUCATION_TUITION",
        is_verified=True,
    )
    db_session.add_all([grant, merchant])
    await db_session.commit()

    # Scenario A1: APPROVED Transaction
    tx_approved = GrantTransaction(
        grant_id=grant.id,
        beneficiary_id=student.id,
        merchant_id=merchant.id,
        amount=Decimal("45000.00"),
        merchant_category="EDUCATION_TUITION",
        decision=TransactionDecision.APPROVED,
        decision_reason="Permitted educational merchant category under ENG-SCH-2026 policy.",
        payment_reference="TXN-MOCK-9918237",
    )
    db_session.add(tx_approved)
    await db_session.commit()
    await db_session.refresh(tx_approved)

    assert tx_approved.decision == TransactionDecision.APPROVED
    assert tx_approved.amount == Decimal("45000.00")
    assert grant.remaining_balance == Decimal("35000.00")


@pytest.mark.asyncio
async def test_ngo_milestone_and_audit_event_representation(db_session: AsyncSession):
    ngo_user = User(
        email="contact@ruralhealthngo.org",
        full_name="Rural Infrastructure Foundation",
        role=UserRole.NGO_ORG,
    )
    program = GrantProgram(
        title="Rural Infrastructure Development Grant",
        code="RURAL-INFRA-2026",
        department="Rural Development Board",
        total_budget=Decimal("100000000.00"),  # 10 Crore INR
    )
    db_session.add_all([ngo_user, program])
    await db_session.commit()

    grant = Grant(
        program_id=program.id,
        beneficiary_id=ngo_user.id,
        grant_number="GRN-NGO-RURAL-001",
        allocated_amount=Decimal("100000000.00"),
        status=GrantStatus.RELEASED,
    )
    db_session.add(grant)
    await db_session.commit()

    milestone1 = GrantMilestone(
        grant_id=grant.id,
        title="Milestone 1: Land Preparation & Excavation",
        milestone_index=1,
        target_amount=Decimal("15000000.00"),  # 1.5 Crore
        status=MilestoneStatus.APPROVED,
    )
    db_session.add(milestone1)
    await db_session.commit()

    audit_event = AuditEvent(
        event_type=AuditEventType.MILESTONE_APPROVED,
        actor_id=ngo_user.id,
        entity_type="GRANT_MILESTONE",
        entity_id=str(milestone1.id),
        event_metadata={"milestone_index": 1, "approved_amount": 15000000.00},
    )
    db_session.add(audit_event)
    await db_session.commit()
    await db_session.refresh(audit_event)

    assert audit_event.event_type == AuditEventType.MILESTONE_APPROVED
    assert audit_event.entity_id == str(milestone1.id)
