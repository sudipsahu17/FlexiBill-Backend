"""Define response model for the endpoint version."""
from pydantic import BaseModel, Field  # type: ignore


class VersionResponse(BaseModel):
    """Response for version endpoint."""
    version: str = Field(..., example="1.0.0")


class BaseResponse(BaseModel):
    """Base response model."""
    message: str = Field(default="API is working fine.")
    status: str = Field(example="success", default="success")
    code: int = Field(example=200, default=200)
    data: dict = Field(example={}, description="Response data", default={})
