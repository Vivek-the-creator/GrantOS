import uuid
from decimal import Decimal
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import String, Integer, Numeric, DateTime, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.enums import MilestoneStatus, VerificationStatus


class GrantMilestone(Base):
    __tablename__ = "grant_milestones"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    grant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("grants.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    milestone_index: Mapped[int] = mapped_column(Integer, nullable=False)
    target_amount: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    status: Mapped[MilestoneStatus] = mapped_column(SQLEnum(MilestoneStatus, name="milestone_status_enum"), default=MilestoneStatus.PENDING, nullable=False)
    approved_by_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    tranche_release_ref: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    grant: Mapped["Grant"] = relationship("Grant", back_populates="milestones")
    approver: Mapped[Optional["User"]] = relationship("User", foreign_keys=[approved_by_id])
    evidences: Mapped[list["MilestoneEvidence"]] = relationship("MilestoneEvidence", back_populates="milestone", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<GrantMilestone index={self.milestone_index} title='{self.title}' amount={self.target_amount} status='{self.status}'>"


class MilestoneEvidence(Base):
    __tablename__ = "milestone_evidences"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    milestone_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("grant_milestones.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    storage_path: Mapped[str] = mapped_column(String(512), nullable=False)
    sha256_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    verification_status: Mapped[VerificationStatus] = mapped_column(SQLEnum(VerificationStatus, name="evidence_verification_status_enum"), default=VerificationStatus.PENDING, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    milestone: Mapped[GrantMilestone] = relationship("GrantMilestone", back_populates="evidences")

    def __repr__(self) -> str:
        return f"<MilestoneEvidence file='{self.file_name}' status='{self.verification_status}'>"
