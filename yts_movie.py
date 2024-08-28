import requests
import json
import urllib

class torrent():
	def __repr__(self):
		return '<torrent object : quality = {} , size = {}\n>'.format(self.quality , self.size) ; 

	def __str__(self):
		return '<torrent object : quality = {} , size = {}\n>'.format(self.quality , self.size) ; 

	def __init__(self , torrent_dict : dict  , name =''):
		self.name = name ; 
		self.url = torrent_dict.get('url')
		self.hash = torrent_dict.get('hash')
		self.quality = torrent_dict.get('quality')
		self.seeds = torrent_dict.get('seeds')
		self.peers = torrent_dict.get('peers')
		self.size = torrent_dict.get('size')
		self.date_uploaded = torrent_dict.get('date_uploaded')


		trackers = [
		'udp://open.demonii.com:1337/announce',
		'udp://tracker.openbittorrent.com:80',
		'udp://tracker.coppersurfer.tk:6969',
		'udp://glotorrents.pw:6969/announce',
		'udp://tracker.opentrackr.org:1337/announce',
		'udp://torrent.gresille.org:80/announce',
		'udp://p4p.arenabg.com:1337',
		'udp://tracker.leechers-paradise.org:6969',
		'http://track.one:1234/announce',
		'udp://track.two:80'
		]

		movie_name_encoded = urllib.parse.urlencode({'dn':self.name}) ; 
		self.magnet = 'magnet:?xt=urn:btih:{}&{}'.format(self.hash , movie_name_encoded) ; 
		for tracker in trackers:
			self.magnet+=('&tr='+tracker)

def get_movie_info(title):
	"""
	Fetches information about a movie from the yts.mx API using the given title.

	Args:
			title: The title of the movie to search for.

	Returns:
			A dictionary containing movie information if found, otherwise None.
	"""
	# Base URL for the YTS API
	base_url = "https://yts.mx/api/v2/list_movies.json"

	# Define query parameters
	params = {
		"query_term": title,
		"limit": 1  # Limit results to only the first movie
	}

	# Send GET request to the API
	response = requests.get(base_url, params=params)

	# Check for successful response
	if response.status_code == 200:
		data = json.loads(response.text)
		movies = data.get('data', {}).get('movies', [])

		# If movie found, return its information
		if movies:
			return movies[0]
		else:
			print(f"Movie '{title}' not found on yts.mx")
	else:
		print(f"Error fetching movie info: {response.status_code}")

	return None

# Example usage
movie_title = "The Shawshank Redemption"
movie_info = get_movie_info(movie_title)

if movie_info:
	print(f"Movie Title: {movie_info['title']}")
	print(f"Year: {movie_info['year']}")
	print(f"Rating: {movie_info['rating']}")
	t = torrent(movie_info['torrents'][0])
	print (f"Magnet: {t.magnet}")
	#print(movie_info)
	# Access other movie information as needed (e.g., synopsis, genres, etc.)
else:
	print("Movie information not available.")