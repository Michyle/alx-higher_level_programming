#!/usr/bin/python3
""" This prints the state object with the name passed as argument"""
import sys
from model_state import Base, State
from sqlalchmey import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'  .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Bsse.metadate.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    new_instance = session.query(State).filter_by(name='Louisana').first()
    print(new_instance.id)
    session.commit()
