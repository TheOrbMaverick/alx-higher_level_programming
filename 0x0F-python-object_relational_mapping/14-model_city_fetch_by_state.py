#!/usr/bin/python3
"""Script to fetch and print all City objects from the
database hbtn_0e_14_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Query all City objects and print them with state name
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State).filter_by(
            id=city.state_id
            ).first().name
        print(f"{state_name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
