from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from connection import Base
from sqlalchemy.orm import relationship


class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    row = Column(Integer)
    col = Column(Integer)

    projection_id = Column(Integer, ForeignKey('projections.id'))
    projection = relationship("Projection", backref="reservations")
