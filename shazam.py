import requests
import json


def shazam(filepath):

    url = "https://api.audd.io/"
    data = {
        "api_token": "78fe81024da2a73ae9e15648e1fee64c",  
        "return": "lyrics,apple_music,spotify",
        }

    with open(filepath, "rb") as audio_file:
        files = {
            "file": audio_file
        }

        response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        data = response.json()
        track = data.get('result', {})
        # print(track)

        if not track:
            return {"error": "No song Identified..."}
        
        return {
            "title" : track.get('title', 'No title available...'),
            "artist" : track.get('artist', 'No artist available...'),
            "album" : track.get('album', 'No album available...'),
            "cover_art" : (track.get('spotify', {}).get('album', {}).get('images', [{}])[0].get('url', 'No picture available')),
            "song_link" : track.get('spotify', {}).get('external_urls', {}).get('spotify', 'No Spotify link available')
        }

       
        # Testing code for songs
        # print("Song information: ")
        # print(cover_art)
        # print(f"Song: {title}")
        # print(f"By {artist}")
        # print(f"Album: {album}")
        # print(f"Song link: {song_link}")
    # else:
    #     print("Error")

# shazam('audio_files/monster.mp3')