import pandas as pd
import scipy.stats as sc
from Spotify_API.theAPI import sp as api


#Reading data in csv format
data = pd.read_csv(r"C:\Users\Victor J. Villadiego\OneDrive\Escritorio\dsEAFIT\Programas\Hit_Song_Predictor\data\data.csv")
data_by_artist = pd.read_csv(r"C:\Users\Victor J. Villadiego\OneDrive\Escritorio\dsEAFIT\Programas\Hit_Song_Predictor\data\data_by_artist.csv")
data_by_genres = pd.read_csv(r"C:\Users\Victor J. Villadiego\OneDrive\Escritorio\dsEAFIT\Programas\Hit_Song_Predictor\data\data_by_genres.csv")
data_by_years = pd.read_csv(r"C:\Users\Victor J. Villadiego\OneDrive\Escritorio\dsEAFIT\Programas\Hit_Song_Predictor\data\data_by_year.csv")
data_w_genres = pd.read_csv(r"C:\Users\Victor J. Villadiego\OneDrive\Escritorio\dsEAFIT\Programas\Hit_Song_Predictor\data\data_w_genres.csv")


data = data.assign(Updated_popularity=0)

cont = 0

for i in data["id"]:
    song_id = i
    filt = data["id"] == song_id
    song_popularity = api.track(song_id)["popularity"]
    data.loc[filt, "Updated_popularity"] = song_popularity
    cont += 1
    if cont % 10000 == 0:
        print(f"Por el momento van {cont} canciones actualizadas")


data.to_csv('data_cleaned.csv', index=False)


