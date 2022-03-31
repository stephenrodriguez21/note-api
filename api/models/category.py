"""Category Model"""

from sqlalchemy import Column, String, ForeignKey, Boolean, Integer, DateTime, func
from sqlalchemy.orm import relationship
from api.database import Base


class Category(Base):

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)