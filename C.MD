# Configuration Instructions

Before running the code, you will need to set up the necessary API keys and authentication credentials. This can be done by modifying the `credentials.ini` file located in the `config` folder. 

The `credentials.ini` file should have the following structure:

| Key | Value |
| --- | --- |
| 'client_id' | '' |
| 'client_secret' | '' |
| 'access_token' | '' |

*Note: The `client_id` and `client_secret` values should be obtained from Spotify, while the `access_token` value should be obtained from LyricsGenius.*



To obtain your own API keys and credentials, follow these steps:

1. Create a Spotify Developer account and register a new application: https://developer.spotify.com/dashboard/applications

2. Note down your `client_id` and `client_secret` from the Spotify Developer Dashboard.

3. Create a Genius account and register a new API Client: https://genius.com/api-clients/new

4. Note down your `access_token` from the Genius API Dashboard.

5. Paste your API keys and credentials in the `credentials.ini` file in the `config` folder.

6. Save the `credentials.ini` file.

Once you have completed these steps, you are ready to run the code!
