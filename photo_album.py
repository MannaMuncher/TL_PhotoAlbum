import requests
import json
import sys

def retrieve_photos(album_number):
    response = requests.get(f"https://jsonplaceholder.typicode.com/photos?albumId={album_number}")

    if response.status_code != 200:
        print("Failed to retrieve photos")
        return None

    photos = json.loads(response.text)
    return photos

def display_photos(photos):
    if not photos:
        return

    print(f"Photos in album {photos[0]['albumId']}")
    for photo in photos:
        print(f"[{photo['id']}] {photo['title']}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: photo-album <album_number>")
        sys.exit(1)

    album_number = sys.argv[1]
    photos = retrieve_photos(album_number)
    display_photos(photos)
