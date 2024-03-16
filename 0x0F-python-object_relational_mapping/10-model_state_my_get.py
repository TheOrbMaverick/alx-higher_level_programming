#!/usr/bin/python3
"""
Script to print the State object with the name passed as
argument from the database hbtn_0e_6_usa.

Usage: ./10-model_state_my_get.py <username> <password> <database> <state_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"""Usage: {sys.argv[0]} <username> <password>
              <database> <state_name>""")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    # Create engine to connect to MySQL database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
        )

    # Create a session maker bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query State object with the given state name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the state ID or "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
