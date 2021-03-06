import json
import requests
import random
from random import shuffle


#Ta funkcja jest tu umieszczona na potrzeby zadania z modulu 14.3
def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYTc2NzIyMjA5ZWJjYTU2MGNiZmU2MDJlMmI1ZTc2MSIsInN1YiI6IjYyN2Y5ZjYyYzkyYzVkMDA2OGFlYmEwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mabgzv7Z5fThTIfaH9Ww45ilYmMRcsrTLKNXAc1nrNk"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()
#koniec funkcji umieszczonej na potrzeby zadania z modulu 14.3



def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYTc2NzIyMjA5ZWJjYTU2MGNiZmU2MDJlMmI1ZTc2MSIsInN1YiI6IjYyN2Y5ZjYyYzkyYzVkMDA2OGFlYmEwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mabgzv7Z5fThTIfaH9Ww45ilYmMRcsrTLKNXAc1nrNk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()



def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"



def get_movies(how_many, list_type):
    #data = get_popular_movies()
    data = get_movies_list(list_type)
    movies = data["results"]
    random.shuffle(movies)
    return movies[:how_many]



def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYTc2NzIyMjA5ZWJjYTU2MGNiZmU2MDJlMmI1ZTc2MSIsInN1YiI6IjYyN2Y5ZjYyYzkyYzVkMDA2OGFlYmEwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mabgzv7Z5fThTIfaH9Ww45ilYmMRcsrTLKNXAc1nrNk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()



def get_single_movie_cast(movie_id, number):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYTc2NzIyMjA5ZWJjYTU2MGNiZmU2MDJlMmI1ZTc2MSIsInN1YiI6IjYyN2Y5ZjYyYzkyYzVkMDA2OGFlYmEwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mabgzv7Z5fThTIfaH9Ww45ilYmMRcsrTLKNXAc1nrNk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"][:number]



def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYTc2NzIyMjA5ZWJjYTU2MGNiZmU2MDJlMmI1ZTc2MSIsInN1YiI6IjYyN2Y5ZjYyYzkyYzVkMDA2OGFlYmEwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mabgzv7Z5fThTIfaH9Ww45ilYmMRcsrTLKNXAc1nrNk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()



def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYTc2NzIyMjA5ZWJjYTU2MGNiZmU2MDJlMmI1ZTc2MSIsInN1YiI6IjYyN2Y5ZjYyYzkyYzVkMDA2OGFlYmEwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mabgzv7Z5fThTIfaH9Ww45ilYmMRcsrTLKNXAc1nrNk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


#Ta funkcja jest tu umieszczona na potrzeby zadania z modulu 14.3

def get_movies_list(list_type):
   return call_tmdb_api(f"movie/{list_type}")

#koniec funkcji umieszczonej na potrzeby zadania z modulu 14.3
