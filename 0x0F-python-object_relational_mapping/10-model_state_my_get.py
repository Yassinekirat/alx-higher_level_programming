#!/usr/bin/python3
"""List all states"""
import sys
from model_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    all = session.query(State)
    found = False
    for state in all:
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = 1
    if found is False:
        print("Not found")
