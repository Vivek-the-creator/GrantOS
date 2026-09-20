import uuid
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class Merchant(Base):
    __tablename__ = "merchants"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    business_name: Mapped[str] = mapped_column(String(255), nullable=False)
    merchant_code: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    mcc: Mapped[str] = mapped_column(String(16), index=True, nullable=False)
    category: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    user: Mapped[Optional["User"]] = relationship("User", back_populates="merchant_profile")
    transactions: Mapped[list["GrantTransaction"]] = relationship("GrantTransaction", back_populates="merchant")

    def __repr__(self) -> str:
        return f"<Merchant code='{self.merchant_code}' name='{self.business_name}' mcc='{self.mcc}'>"
