#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa.

Usage: ./8-model_state_fetch_first.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]

    # Create engine to connect to MySQL database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
        )

    # Create a session maker bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Check if the first_state is None
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
