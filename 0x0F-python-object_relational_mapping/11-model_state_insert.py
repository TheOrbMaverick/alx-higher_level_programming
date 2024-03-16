#!/usr/bin/python3
"""
Script to add the State object "Louisiana" to the database hbtn_0e_6_usa.

Usage: ./11-model_state_insert.py <username> <password> <database>
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

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session maker bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create the State object and add it to the session
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Print the new state's ID
    print(new_state.id)

    # Close the session
    session.close()
