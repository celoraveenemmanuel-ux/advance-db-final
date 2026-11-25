import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
movies = db.collection("movies")

COLUMNS = ["movie_id", "movie_title", "movie_director", "movie_release", "movie_genre",
           "movie_boxoffice", "movie_country", "movie_budget", "movie_runtime_minutes",
           "movie_rating"]

search = input("Enter movie title: ")

if search == "":
    print("HAHAHAHAH Mango")
else:
    matches = [
        doc for doc in movies.stream()
        if search.lower() in str(doc.to_dict().get("movie_title", "")).lower()
    ]

    if not matches:
        print("Movie not found")
    else:
        print(f"Found {len(matches)} movies: ")
        for doc in matches:
            movie = doc.to_dict()
            print("-")
            for column in COLUMNS:
                value = movie.get(column)
                print(f" {column}: {'N/A' if value is None else value}")