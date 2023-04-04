# Usage

This script can be used to automate various Spotify tasks.

## Getting started

Before running the script, you need to set up the necessary credentials in the `config/credentials.ini` file. The `client_id` and `client_secret` are for Spotify, and the `access_token` is for LyricsGenius.

## Running the script

To run the script, simply execute the `main.py` file with the desired arguments.

### Arguments

The script takes the following arguments:

- `-ps`, `--playlists`: get all playlists attributes.
- `-s`, `--songs <playlist_name>`: get all songs from a specific playlist.
- `-l`, `--lyrics`: get the lyrics for the user's currently playing track.

### Examples

Get all playlist attributes:

Here's an example of how you can use the `main.py` script:

```bash
python3 main.py -ps
```

This will print a table with all your playlists attributes.


Get all songs from a specific playlist:


```bash
python3 main.py -s <playlist_name>
```

Get lyrics for the user's currently playing track:
```bash
python3 main.py -l
```
