#!/usr/bin/python3
"""
Script to list all State objects containing the
letter 'a' from the database hbtn_0e_6_usa.

Usage: ./9-model_state_filter_a.py <username> <password> <database>
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

    # Query all State objects containing the letter 'a'
    filtered_states = session.query(State).filter(
        State.name.like('%a%')
        ).order_by(State.id).all()

    # Print the filtered states
    for state in filtered_states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
