#!/usr/bin/python3
"""First city model"""

from sqlalchemy import MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base(metadata=MetaData())


class City(Base):
    """classe City"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('States.id'), nullable=False)