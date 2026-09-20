from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.config import settings
from app.core.database import get_db
from app.schemas.health import HealthResponse, ReadinessResponse

router = APIRouter(tags=["Health & Infrastructure"])


@router.get("/health", response_model=HealthResponse, summary="Service Health Check")
async def health_check():
    """
    Returns basic application engine health status.
    """
    return HealthResponse(
        status="ok",
        service=settings.PROJECT_NAME,
        phase=2,
        version=settings.VERSION,
    )


@router.get(
    "/health/readiness",
    response_model=ReadinessResponse,
    summary="Database Readiness & Connectivity Check",
)
async def readiness_check(db: AsyncSession = Depends(get_db)):
    """
    Executes a SELECT 1 query against the database via SQLAlchemy async session to verify connectivity.
    """
    try:
        result = await db.execute(text("SELECT 1"))
        val = result.scalar()
        if val != 1:
            raise ValueError("Unexpected query response from database.")
        
        return ReadinessResponse(
            status="ready",
            database="connected",
            timestamp=datetime.now(timezone.utc),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database readiness check failed: {str(e)}",
        )
