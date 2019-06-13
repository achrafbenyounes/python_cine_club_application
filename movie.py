import os
import json

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

class Movie:

    def __init__(self, title):
        self.title = title.title()
    
    def __str__(self):
        return self.title

    # This is a gette method, to read from a json file containg the movies
    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    
    # This is a setter method, it aims to write in the data json file containg the movies
    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)




m1 = Movie("harry potter")

m1._write_movies(["Harry Potter", "Le Seigneur Des Anneaux", "Avengers", "Dark", "Lucifer"])

print(m1._get_movies())