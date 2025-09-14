from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from flexibill.app.db import Base


class User(Base):
    """User model representing application users."""

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    mobile_number = Column(String, unique=True, index=True, nullable=False)
    device_id = Column(String, nullable=False)
    licenses = relationship(
        "License", backref="user"
    )  # 1-to-many: user.licenses gives all licenses for a user
