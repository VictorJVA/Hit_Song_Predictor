#Importamos librerías de Spotify(Spotify for developers)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Guardamos en una variable nuestro client_id y client_secret
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="4007b4a4055d44478ac95dba0bfb28fd",
                                                           client_secret="02d214197de54bf6bf0deb21b8f19f9f"))


#Ejemplo canción
song_id = "0R6NfOiLzLj4O5VbYSJAjf"
song_audio_features = sp.audio_features(song_id)
song_info = sp.track(song_id)

artist_id = "3Me35AWHCGqW4sZ7bWWJt1"
artist_info = sp.artist(artist_id)
artist_more_info = sp.artist_related_artists(artist_id)

playlist_id = "37i9dQZEVXbMDoHDwVN2tF"
playlist_info = sp.playlist_tracks(playlist_id)

print("Información artista y algunas cosas de la canción\n")
print(song_info)
print("Datos del artista\n")
print(artist_info)
print("Datos análisis de la canción\n")
print(song_audio_features)
print("Playlist Info\n")
print(artist_more_info)
#print(playlist_info)