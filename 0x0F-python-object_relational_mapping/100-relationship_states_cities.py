#!/usr/bin/python3
"""Script to create the State "California" with the City "San Francisco"."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State, City


def main(username, password, database):
    # Define the database connection string
    db_string = f"mysql://{username}:{password}@localhost:3306/{database}"

    # Create an engine and bind the Base class to it
    engine = create_engine(db_string)
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State instance for California
    california = State(name="California")

    # Create a new City instance for San Francisco and link it to California
    san_francisco = City(name="San Francisco", state=california)

    # Add both instances to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the session to save changes to the database
    session.commit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python file <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    main(username, password, database)
