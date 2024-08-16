from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('GOOGLE_API_KEY')

def main():
    playlist_id = "PLW2VEpJ8QmP4bNQ3gt8aqgvJFHOsYsPE_"

    # Create a YouTube API client
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    try:
        # Call the playlistItems().list method to retrieve playlist items
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50  # Adjust this number as needed
        )
        response = request.execute()

        # Print video names
        for item in response.get('items', []):
            print(item['snippet']['title'])

        # Handle pagination if there are more results
        while 'nextPageToken' in response:
            request = youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=response['nextPageToken']
            )
            response = request.execute()
            for item in response.get('items', []):
                print(item['snippet']['title'])

    except HttpError as e:
        print(f"An HTTP error occurred: {e}")

if __name__ == "__main__":
    main()