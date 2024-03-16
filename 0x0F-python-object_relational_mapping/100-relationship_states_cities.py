#!/usr/bin/python3
"""Script to create the State "California" with the City "San Francisco"."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
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

    # Create California state and San Francisco city
    california = State(name='California')
    san_francisco = City(name='San Francisco', state=california)

    # Add California and San Francisco to the session and commit
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close the session
    session.close()
