import requests

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('OMDB_API_KEY')

movie_title = "The Instigators"
url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie_title}"

response = requests.get(url)
data = response.json()

if data.get("Response") == "True":
    release_date = data.get("Released", "Release date not available")
    print(f"Release date of '{movie_title}': {release_date}")
else:
    print(f"Movie '{movie_title}' not found or error in API response")

print(data)