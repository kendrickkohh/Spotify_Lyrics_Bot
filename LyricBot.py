#Source: https://www.youtube.com/watch?v=cU8YH2rhN6A&t=1129s
import json
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius

#----- SPOTIFY AND GENIUS TOKENS ------
SPOTIFYclientID = "eedecfb44c9a4160aba8f55b18c9230d"
SPOTIFYclientsecret = "46ab59a2119c4c0fbd6272bc516554a8"
REDIRECTURI = "https://www.google.com"
GENIUStoken = "WywbmDXksHJO6XeM_tQO26J3IlJpS5fL5sivuCUScCpyeh7tnEVw5wzh6B9w0_6-"

#----- OBTAINING TOKEN DICTIONARY -----
scope = "user-read-currently-playing" #Spotify scope

oauth_object = spotipy.SpotifyOAuth(client_id = SPOTIFYclientID, client_secret = SPOTIFYclientsecret,
                                    redirect_uri = REDIRECTURI, scope = scope) #Spotify Oauth class, creating an Oauth object

token_dict = oauth_object.get_cached_token() #Use get_access_token to access token_dict, which goes to REDIRECTURI

token = token_dict['access_token'] #Acquire access token through terminal

spotify_object = spotipy.Spotify(auth=token) #Create spotify_object using the spotify access token

genius_object = lyricsgenius.Genius(GENIUStoken) #Create genius_object

#----- MAIN PROGRAM LOOP -----
while True:
    current = spotify_object.currently_playing() #Create current variable that uses to the spotify.currently_playing() function, to look at currently playing song
                                                 #Use print(json.dumps(current,sort_keys=False,indent=4)) to view dictionary
    status = current['currently_playing_type'] #Obtain status of song playing, used to determine if a track of ad is playing
    
    if status == 'track':
        artist_name1 = current['item']['album']['artists'][0]['name'] #Attain artist_name from dictionary
        song_title1 = current['item']['name'] #Obtain song title from dictionary
    
        skip = False

        song = genius_object.search_song(title=song_title1, artist=artist_name1) #Searches song on genius
        
        try:
            lyrics=song.lyrics #Obtain song lyrics
            print()
            print('(╯°□°)╯ ┻━┻  (*^-^*)  \(^-^)/  ( ͡° ͜ʖ ͡°)  (╯°□°)╯ ┻━┻  (*^-^*)  \(^-^)/  ( ͡° ͜ʖ ͡°)') #yes
            print()
            print(lyrics)
            print()

        except:
            print()
            print(">> Lyrics were not found")
            print()
            
        #----- Detects user skipping songs -----   
        try:
            while skip == False: #Detects user skipping songs
                current1 = spotify_object.currently_playing() #Create second "current" variable
                song_title2 = current1['item']['name'] #Retrieve second song title for comparison
                artist_name2 = current1['item']['album']['artists'][0]['name'] #Retrieve second artist name for comparison
            
                if song_title2 != song_title1 or artist_name2 != artist_name1: #Compare 2nd artist and song title to first,
                    skip = True                                                #if different, loop exits and prints new lyrics
                else:
                    skip = False #Else the loops just keeps running until song title changes
        except:
            continue
        
    elif status == 'ad': #Loop for ads
        #----- Detects when ad end -----   
        while skip == False:
            current1 = spotify_object.currently_playing()
            status2 = current1['currently_playing_type']
            
            if status2 == 'ad':
                skip = False
            else:
                skip = True
