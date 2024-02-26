#!/usr/bin/python3
"""relation_states_cities module"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    california = State(name='California')

    san_francisco = City(name='San Francisco', state=california)

    session.add(california)
    session.add(san_francisco)

    session.commit()
    session.close()
