import uuid
from decimal import Decimal
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import String, Text, Numeric, DateTime, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.enums import TransactionDecision


class GrantTransaction(Base):
    __tablename__ = "grant_transactions"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    grant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("grants.id", ondelete="RESTRICT"), nullable=False)
    beneficiary_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    merchant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("merchants.id", ondelete="RESTRICT"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(8), default="INR", nullable=False)
    merchant_category: Mapped[str] = mapped_column(String(64), nullable=False)
    decision: Mapped[TransactionDecision] = mapped_column(SQLEnum(TransactionDecision, name="transaction_decision_enum"), nullable=False)
    decision_reason: Mapped[str] = mapped_column(Text, nullable=False)
    payment_reference: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    blockchain_tx_hash: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    grant: Mapped["Grant"] = relationship("Grant", back_populates="transactions")
    beneficiary: Mapped["User"] = relationship("User", foreign_keys=[beneficiary_id])
    merchant: Mapped["Merchant"] = relationship("Merchant", back_populates="transactions")

    def __repr__(self) -> str:
        return f"<GrantTransaction amount={self.amount} decision='{self.decision}'>"
