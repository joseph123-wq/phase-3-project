import argparse
from app.models import Artist, Artwork
from app.database import session

def add_artist(name, age, birthplace, style_of_work):
    new_artist = Artist(name=name, age=age, birthplace=birthplace, style_of_work=style_of_work)
    session.add(new_artist)
    session.commit()
    print(f"Added artist: {name}")

def add_artwork(artist_name, year_of_making, unique_title, style_of_art, price):
    artist = session.query(Artist).filter_by(name=artist_name).first()
    if artist:
        new_artwork = Artwork(artist_id=artist.id, year_of_making=year_of_making, unique_title=unique_title, style_of_art=style_of_art, price=price)
        session.add(new_artwork)
        session.commit()
        print(f"Added artwork: {unique_title} by {artist_name}")
    else:
        print(f"Artist {artist_name} not found.")










