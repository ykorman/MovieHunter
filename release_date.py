import requests

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('OMDB_API_KEY')

def get_release_date(title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    response = requests.get(url)
    data = response.json()

    release_date = None
    if data.get("Response") == "True":
        release_date = data.get("Released", None)

    return release_date

def main():
    movie_title = "The Instigators"
    release_date = get_release_date(movie_title)
    if release_date != None:
        print(f"Release date of '{movie_title}': {release_date}")
    else:
        print(f"Movie '{movie_title}' not found or error in API response")

if __name__ == "__main__":
    main()