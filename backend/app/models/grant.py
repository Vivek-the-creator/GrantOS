import uuid
from decimal import Decimal
from datetime import datetime, timezone
from typing import Optional, Any
from sqlalchemy import String, Text, Numeric, DateTime, Enum as SQLEnum, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.enums import GrantProgramStatus, GrantStatus


class GrantProgram(Base):
    __tablename__ = "grant_programs"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    department: Mapped[str] = mapped_column(String(128), nullable=False)
    total_budget: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(8), default="INR", nullable=False)
    status: Mapped[GrantProgramStatus] = mapped_column(SQLEnum(GrantProgramStatus, name="grant_program_status_enum"), default=GrantProgramStatus.DRAFT, nullable=False)
    rules_policy_json: Mapped[Optional[Any]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    grants: Mapped[list["Grant"]] = relationship("Grant", back_populates="program")
    applications: Mapped[list["ScholarshipApplication"]] = relationship("ScholarshipApplication", back_populates="program")

    def __repr__(self) -> str:
        return f"<GrantProgram code='{self.code}' budget={self.total_budget} {self.currency}>"


class Grant(Base):
    __tablename__ = "grants"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    program_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("grant_programs.id", ondelete="RESTRICT"), nullable=False)
    beneficiary_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    grant_number: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    allocated_amount: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    spent_amount: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=Decimal("0.00"), nullable=False)
    currency: Mapped[str] = mapped_column(String(8), default="INR", nullable=False)
    status: Mapped[GrantStatus] = mapped_column(SQLEnum(GrantStatus, name="grant_status_enum"), default=GrantStatus.CREATED, nullable=False)
    valid_from: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    valid_until: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    blockchain_grant_hash: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    program: Mapped[GrantProgram] = relationship("GrantProgram", back_populates="grants")
    beneficiary: Mapped["User"] = relationship("User", back_populates="grants", foreign_keys=[beneficiary_id])
    transactions: Mapped[list["GrantTransaction"]] = relationship("GrantTransaction", back_populates="grant")
    milestones: Mapped[list["GrantMilestone"]] = relationship("GrantMilestone", back_populates="grant")

    @property
    def remaining_balance(self) -> Decimal:
        return self.allocated_amount - self.spent_amount

    def __repr__(self) -> str:
        return f"<Grant number='{self.grant_number}' allocated={self.allocated_amount} status='{self.status}'>"
