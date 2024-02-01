import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="4007b4a4055d44478ac95dba0bfb28fd",
                                                           client_secret="02d214197de54bf6bf0deb21b8f19f9f"))


song_id = "7xPhfUan2yNtyFG0cUWkt8"
song_audio_features = sp.audio_features(song_id)

song_info = sp.track(song_id)

print(song_info)
print(song_audio_features)





