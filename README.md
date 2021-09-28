# Spotify_Lyrics_Bot
Automates lyrics production for unique Spotify users

For usage,
1. Ensure you have attained your own Spotify and Lyrics Genius Client ID and Client secrets

2. Once done, run the program with token_dict = oauth_object.get_access_token() instead of token_dict = oauth_object.get_cached_token() (LINE 20)

3. Copy and paste the URL of google that is opened into your terminal when prompted and ensure that there is a .cache file in the file the program is in

4. Change back token_dict to token_dict = oauth_object.get_cached_token() and run the program while listening to your Spotify
