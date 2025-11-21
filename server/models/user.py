from db import Base
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False) # encrypted
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)