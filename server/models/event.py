from db import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

class User(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey=("users.user_id"))
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    time = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)