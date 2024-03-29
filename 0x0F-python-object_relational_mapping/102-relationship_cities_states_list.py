#!/usr/bin/python3
""" relationship_state_client module """
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, declarative_base
from sys import argv


Base = declarative_base()


class State(Base):
    """ class state """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete")


class City(Base):
    """ city class """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")


if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
