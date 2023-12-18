#!/usr/bin/python3
"""
Script for inserting a new state, "Louisiana," into the database.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)

    for row in session.query(State).filter(State.name.like("%a%")).all():
        session.delete(row)
    session.commit()

    session.close()
