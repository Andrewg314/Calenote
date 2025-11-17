from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
import os

# set up engine
engine = create_engine(os.getenv('DATABASE_URL'))

class Base(DeclarativeBase):
    pass