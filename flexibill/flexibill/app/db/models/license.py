from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Sequence, String

from flexibill.app.db import BaseModel


class License(BaseModel):
    """License model representing user licenses."""

    id = Column(Integer, Sequence("license_id_seq"), primary_key=True)
    key = Column(String, unique=True, index=True)
    valid_till = Column(DateTime, nullable=False)
    user_id = Column(
        Integer, ForeignKey("user.id"), nullable=False
    )  # ForeignKey to user table
    issued_by = Column(String, nullable=False)
    license_type = Column(String)
    is_active = Column(Boolean, default=True)
    comments = Column(String, nullable=True)
