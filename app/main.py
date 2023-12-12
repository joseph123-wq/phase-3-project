from app.database import create_database
from app.cli import add_artist, add_artwork

if __name__ == "__main__":
    create_database()  

   
    add_artist("Leonardo da Vinci", 67, "Vinci, Italy", "Renaissance")
    add_artwork("Leonardo da Vinci", 1503, "Mona Lisa", "Oil painting", 100000000)



