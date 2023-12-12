from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    birthplace = Column(String)
    style_of_work = Column(String)
    artworks = relationship('Artwork', back_populates='artist')

class Artwork(Base):
    __tablename__ = 'artworks'
    id = Column(Integer, primary_key=True)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    year_of_making = Column(Integer)
    unique_title = Column(String)
    style_of_art = Column(String)
    price = Column(Integer)
    artist = relationship('Artist', back_populates='artworks')




