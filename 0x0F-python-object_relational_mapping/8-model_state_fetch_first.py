#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchmey import (create_enine)
from sqlachemy.orm import sessionmaker

if __name__ == "__main__":
    enine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=enine)
    session = Session()(State).first()
    object_data = session.query
    if object_data is None:
        print("Nothing")
    else:
        print(object_data.id, object_data.name, sep=": ")
