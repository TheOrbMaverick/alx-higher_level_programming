#!/usr/bin/python3
"""Define the State class with a relationship to cities."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City

class State(Base):
    """Represents a state in the database."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    def __repr__(self):
        """Return the string representation of the State instance."""
        return f"<State(id={self.id}, name={self.name})>"
