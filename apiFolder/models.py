import datetime

from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), index=True)
    idade = Column(Integer, index=True)
    create_date = Column(DateTime, default=datetime.datetime.utcnow())