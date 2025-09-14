"""Define the base sqlalchemy model class."""

# mypy: ignore-errors
import datetime as dt

from sqlalchemy import Column, DateTime, Integer, Sequence, String, inspect
from sqlalchemy.ext.declarative import as_declarative, declared_attr


class TimestampMixin:
    created_time = Column(DateTime, default=dt.datetime.now(dt.timezone.utc))
    last_updated_time = Column(
        DateTime,
        default=dt.datetime.now(dt.timezone.utc),
        onupdate=dt.datetime.now(dt.timezone.utc),
    )


class AuditMixin:
    created_by = Column(String, nullable=True)
    last_updated_by = Column(String, nullable=True)


@as_declarative()
class Base:
    """Base table class"""

    @declared_attr
    def __tablename__(cls) -> str:
        """Generate __tablename__ automatically"""
        return cls.__name__.lower()

    def __repr__(self) -> str:
        """Generate a repr of the object."""
        return f"<{self.__class__.__name__}(id={self.id})>"

    def _asdict(self):
        """Convert extract record to dict."""
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class BaseModel(Base, TimestampMixin, AuditMixin):
    """Base table class with timestamp and audit mixins"""

    __abstract__ = True
    id = Column(
        Integer, Sequence("id_seq", start=1000), primary_key=True, autoincrement=True
    )
