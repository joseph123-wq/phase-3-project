from models import Artist, Artwork
from database import session, create_database 

def add_artist():
    name = input("Enter artist's name: ")
    age = int(input("Enter artist's age: "))
    birthplace = input("Enter artist's birthplace: ")
    style_of_work = input("Enter artist's style of work: ")

    new_artist = Artist(name=name, age=age, birthplace=birthplace, style_of_work=style_of_work)
    session.add(new_artist)
    session.commit()
    print(f"Added artist: {name}")

def add_artwork():
    artist_name = input("Enter artist's name: ").strip().lower()  
    year_of_making = int(input("Enter year of making: "))
    unique_title = input("Enter unique title: ")
    style_of_art = input("Enter style of art: ")
    price = int(input("Enter price: "))

    artist = session.query(Artist).filter(Artist.name.ilike(artist_name)).first()  
    if artist:
        new_artwork = Artwork(artist_id=artist.id, year_of_making=year_of_making, unique_title=unique_title,
                              style_of_art=style_of_art, price=price)
        session.add(new_artwork)
        session.commit()
        print(f"Added artwork: {unique_title} by {artist_name}")
    else:
        print(f"Artist {artist_name} not found.")

def delete_artwork_by_title():
    title = input("Enter the unique title of the artwork to delete: ")

    artwork = session.query(Artwork).filter(Artwork.unique_title.ilike(title)).first()
    if artwork:
        session.delete(artwork)
        session.commit()
        print(f"Artwork '{title}' deleted successfully.")
    else:
        print(f"Artwork '{title}' not found.")

def update_artwork():
    title = input("Enter the unique title of the artwork to update: ")

    artwork = session.query(Artwork).filter(Artwork.unique_title.ilike(title)).first()
    if artwork:
        print(f"Current details of '{title}':")
        print(f"Year of making: {artwork.year_of_making}")
        print(f"Style of art: {artwork.style_of_art}")
        print(f"Price: {artwork.price}")

        new_year_of_making = int(input("Enter new year of making (press Enter to keep current): ") or artwork.year_of_making)
        new_style_of_art = input("Enter new style of art (press Enter to keep current): ") or artwork.style_of_art
        new_price = int(input("Enter new price (press Enter to keep current): ") or artwork.price)

        artwork.year_of_making = new_year_of_making
        artwork.style_of_art = new_style_of_art
        artwork.price = new_price

        session.commit()
        print(f"Artwork '{title}' updated successfully.")
    else:
        print(f"Artwork '{title}' not found.")

def view_all_data():
    artists = session.query(Artist).all()
    artworks = session.query(Artwork).all()

    print("----- Artists -----")
    for artist in artists:
        print(f"ID: {artist.id}, Name: {artist.name}, Age: {artist.age}, Birthplace: {artist.birthplace}, Style of Work: {artist.style_of_work}")

    print("\n----- Artworks -----")
    for artwork in artworks:
        print(f"ID: {artwork.id}, Artist ID: {artwork.artist_id}, Title: {artwork.unique_title}, Year of Making: {artwork.year_of_making}, Style of Art: {artwork.style_of_art}, Price: {artwork.price}")

if __name__ == "__main__":
    create_database()  
    while True:
        command = input("Enter command (add_artist, add_artwork, delete_artwork, update_artwork, view_all, 'exit' to quit): ").strip().lower()

        if command == "add_artist":
            add_artist()
        elif command == "add_artwork":
            add_artwork()
        elif command == "delete_artwork":
            delete_artwork_by_title()
        elif command == "update_artwork":
            update_artwork()
        elif command == "view_all":
            view_all_data()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please enter 'add_artist', 'add_artwork', 'delete_artwork', 'update_artwork', 'view_all', or type 'exit' to quit.")

















