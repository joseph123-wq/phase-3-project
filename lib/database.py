from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URI = 'sqlite:///art_gallery.db'
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

def create_database():
    Base.metadata.create_all(engine)



