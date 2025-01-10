import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import spotipy

load_dotenv()

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

url = f"https://www.billboard.com/charts/hot-100/{date}/"
# url = f"https://www.billboard.com/charts/hot-100/2003-08-20/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url=url, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_title = [title.getText().strip() for title in soup.select(selector="li h3#title-of-a-story")]
print(song_title)


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://example.com"

spotipy_auth = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID,
                                           client_secret=CLIENT_SECRET,
                                           redirect_uri=REDIRECT_URI,
                                           cache_path="token.txt",
                                           scope="playlist-modify-private")
sp = spotipy.Spotify(auth_manager=spotipy_auth)
user_id = sp.current_user()["id"]
print(user_id)

song_uri = []
for name in song_title:
    try:
        song_uri.append(sp.search(q=f"track: {name} year: {date[:4]}", type='track')['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{name} does not exist in Spotify. Skipped.")
print(song_uri)

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)['id']
sp.playlist_add_items(playlist_id=playlist_id, items=song_uri)
