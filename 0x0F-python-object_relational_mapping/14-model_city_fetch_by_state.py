#!/usr/bin/python3
""" state_city module"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State
from model_city import City

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    session = Session(engine)

    for state, city in session.query(State, City)\
            .filter(State.id == City.state_id).order_by(City.id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
