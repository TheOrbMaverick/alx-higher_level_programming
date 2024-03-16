#!/usr/bin/python3
"""
Script to change the name of a State object from the database hbtn_0e_6_usa.

Usage: ./12-model_state_update_id_2.py <username> <password> <database>
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

    # Query the State with ID 2 and update its name
    state_id = 2
    state_to_update = session.query(State).filter_by(id=state_id).first()
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
        print(f"State name updated successfully for ID {state_id}")
    else:
        print(f"State with ID {state_id} not found")

    # Close the session
    session.close()
