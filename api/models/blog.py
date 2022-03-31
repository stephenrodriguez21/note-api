"""Blog Model"""

from enum import Enum
from sqlalchemy import Column, String, ForeignKey, Boolean, Integer, DateTime, func
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy.orm import relationship

from api.database import Base

class BlogStatus(Enum):
    CREATED = 'created'
    PENDING_VERIFICATION = 2
    VERIFIED = 3
    REJECTED = 4


class Category(Base):

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class Blog(Base):

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    content = Column(String)
    status = Column(
        ChoiceType(BlogStatus), default=BlogStatus.CREATED
    )
    author_id = Column(Integer, ForeignKey("authors.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    is_active = Column(Boolean, default=True)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    updated_time = Column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )

    # Relationship
    author = relationship("Author")
