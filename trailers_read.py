from googleapiclient.discovery import build
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get('GOOGLE_API_KEY')

# Set up the YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# List of channel IDs
channel_ids = [
    'UCi8e0iOVk1fEOogdfu4YgfA',  # Movieclips Trailers
    'UCzcRQ3vRNr6fJ1A9rqFn7QA',  # Sony Pictures Entertainment
    # Add more channel IDs here
]

def get_latest_trailer(channel_id):
    # Calculate the date 30 days ago
    thirty_days_ago = (datetime.now() - timedelta(days=30)).isoformat() + 'Z'

    # Search for videos from the channel
    search_response = youtube.search().list(
        channelId=channel_id,
        type='video',
        order='date',
        publishedAfter=thirty_days_ago,
        part='id,snippet',
        maxResults=50
    ).execute()

    # Find the first video with 'trailer' in the title
    for item in search_response['items']:
        title = item['snippet']['title'].lower()
        if 'trailer' in title:
            return {
                'title': item['snippet']['title'],
                'video_id': item['id']['videoId'],
                'published_at': item['snippet']['publishedAt'],
                'channel_title': item['snippet']['channelTitle']
            }
    
    return None

# Fetch latest trailers from all channels
latest_trailers = []
for channel_id in channel_ids:
    trailer = get_latest_trailer(channel_id)
    if trailer:
        latest_trailers.append(trailer)

# Print the results
for trailer in latest_trailers:
    print(f"Channel: {trailer['channel_title']}")
    print(f"Title: {trailer['title']}")
    print(f"Video ID: {trailer['video_id']}")
    print(f"Published at: {trailer['published_at']}")
    print("---")
    