#!/usr/bin/python3
"""state model
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Class State """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade = "all, delete")
