#!/usr/bin/python3
""" Prints the first State object from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session: session = Session()

    first = session.query(State).first()

    try:
        print("{}: {}".format(first.id, first.name))
    except None:
        print("Nothing")
    finally:
        session.close()
