from pydantic import BaseModel, Field
from datetime import datetime


class HealthResponse(BaseModel):
    status: str = Field(..., json_schema_extra={"example": "ok"})
    service: str = Field(..., json_schema_extra={"example": "GrantOS API Engine"})
    phase: int = Field(..., json_schema_extra={"example": 2})
    version: str = Field(..., json_schema_extra={"example": "0.2.0"})


class ReadinessResponse(BaseModel):
    status: str = Field(..., json_schema_extra={"example": "ready"})
    database: str = Field(..., json_schema_extra={"example": "connected"})
    timestamp: datetime
