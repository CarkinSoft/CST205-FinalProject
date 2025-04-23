import requests
import json


def shazam(filepath):

    url = "https://shazam-api-free.p.rapidapi.com/shazam/recognize/"
    headers = {
        "x-rapidapi-host": "shazam-api-free.p.rapidapi.com",
        "x-rapidapi-key": "d3c1ecdc01msh60fe3839e71f890p1b9447jsn1908d295c18c"
    }

    with open(filepath, "rb") as audio_file:
        files = {
            "upload_file": audio_file
        }

        response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        data = response.json()
        track = data.get('track', {})
        
        title = track.get('title', 'No title available...')
        artist = track.get('subtitle', 'No artist available...')
        album = track.get('album', 'No album available...')
        cover_art = track.get('images', {}).get('coverart', 'No picture available')
        info_url = track.get('share', {}).get('href', 'No link available')
        
        # print("Song information: ")
        # print(cover_art)
        # print("Song: " + title)
        # print("By " + artist)
        # print("Album: " + album)
        # print("Further info: " + info_url)
    else:
        print("Error")