#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    states = session.query(State).filter(State.name.like((argv[4],))).all()
    if states:
        for state in states:
            print(f"{state.id}")
    else:
        print("Not found")

    session.close()
