# Hit Song Predictor

## Overview

The **Hit Song Predictor** is a project that utilizes the Spotify API to gather data on various musical attributes of tracks. The goal is to predict whether a song has the potential to be a hit based on its acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, and valence.

## Spotify API Attributes

### `acousticness`
- Type: Number (Float)
- Range: 0 - 1
- Description: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
- Example: 0.00242

### `danceability`
- Type: Number (Float)
- Range: 0 - 1
- Description: Describes how suitable a track is for dancing based on a combination of musical elements. 0.0 is least danceable, 1.0 is most danceable.
- Example: 0.585

### `duration_ms`
- Type: Integer
- Description: The duration of the track in milliseconds.
- Example: 237040

### `energy`
- Type: Number (Float)
- Range: 0 - 1
- Description: Represents a perceptual measure of intensity and activity. Energetic tracks feel fast, loud, and noisy.
- Example: 0.842

### `instrumentalness`
- Type: Number (Float)
- Range: 0 - 1
- Description: Predicts whether a track contains no vocals. The closer to 1.0, the greater likelihood the track contains no vocal content.
- Example: 0.00686

### `key`
- Type: Integer
- Range: -1 - 11
- Description: The key the track is in. Integers map to pitches using standard Pitch Class notation.
- Example: 9

### `liveness`
- Type: Number (Float)
- Range: 0 - 1
- Description: Detects the presence of an audience in the recording. Higher values represent an increased probability that the track was performed live.
- Example: 0.0866

### `loudness`
- Type: Number (Float)
- Range: -60 to 0 dB
- Description: The overall loudness of a track in decibels (dB). Useful for comparing relative loudness of tracks.
- Example: -5.883

### `mode`
- Type: Integer
- Description: Indicates the modality (major or minor) of a track. 1 for major, 0 for minor.
- Example: 0

### `speechiness`
- Type: Number (Float)
- Range: 0 - 1
- Description: Detects the presence of spoken words in a track. Higher values indicate more speech-like content.
- Example: 0.0556

### `tempo`
- Type: Number (Float)
- Description: The overall estimated tempo of a track in beats per minute (BPM).
- Example: 118.211

### `time_signature`
- Type: Integer
- Range: 3 - 7
- Description: An estimated time signature. Specifies how many beats are in each bar.
- Example: 4

### `valence`
- Type: Number (Float)
- Range: 0 - 1
- Description: A measure describing the musical positiveness conveyed by a track.
- Example: 0.428

## Usage

To use the Hit Song Predictor, you need to gather the required attributes from the Spotify API for a given track. Once you have the data, you can input it into the prediction model to assess the likelihood of the song becoming a hit.

**Note:** Ensure that you have the necessary access token to retrieve audio analysis data from the Spotify API.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as needed.


