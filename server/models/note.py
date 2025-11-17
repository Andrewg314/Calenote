from db import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Date, DateTime

class Note(Base):
    __tablename__ = "notes"

    note_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey=("users.user_id"))
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)