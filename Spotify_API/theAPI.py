# Import Spotify libraries (Spotify for developers)
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Save our client_id and client_secret in a variable for communication with the API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="4007b4a4055d44478ac95dba0bfb28fd",
                                                           client_secret="02d214197de54bf6bf0deb21b8f19f9f"))
