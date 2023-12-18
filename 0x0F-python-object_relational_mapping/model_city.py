#!/usr/bin/python3
"""city module """
from model_state import Base
from sqlalchemy import Integer, String, Column
from sqlalchemy.sql.schema import ForeignKey


class City(Base):
    """ Class City """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
