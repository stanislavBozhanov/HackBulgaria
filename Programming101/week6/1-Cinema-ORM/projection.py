from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connection import Base


class Projection(Base):
    __tablename__ = 'projections'
    id = Column(Integer, primary_key=True)
    type_ = Column(String)
    date_ = Column(Date)
    time_ = Column(Time)

    movie_id = Column(Integer, ForeignKey('movies.id'))
    movie = relationship("Movie", backref="projections")
