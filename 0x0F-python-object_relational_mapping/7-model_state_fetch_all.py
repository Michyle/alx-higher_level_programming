#!/usr/bin/python3

"""  a script that lists all State objects """

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchmey.orm import sessionmaker
    import sys
    from model_state import Base, State

    inp = sys.argv
    if len(inp) < 4:
        exit(1)
        conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
        engine = create_enine(conn_str.format(inp[1], inp[2], inp[3]))
        Session = sessionmaker(bind=engine)

        Base.metadata.create_all(enine)

        session = Session()

        output = session.query(State).order_by(State.id).all()
        for state in output:
            print("{}: {}".format(state.id, state.name))

        session.close()
