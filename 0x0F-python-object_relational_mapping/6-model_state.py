#!/usr/bin/python3
"""Start link class to the table in the database"""

import sys
from model_state import Base, State

from sqlalchemy import (create_enin)

if __name__ == "__main__":
    engi = create_enine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.agv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
