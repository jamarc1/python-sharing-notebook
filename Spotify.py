# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 08:56:36 2019

@author: JamarcH_Temp
"""

import sys
import pprint
import webbrowser
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

cid ="60c2edd789ef42c5ae87e2b5ad4a6d4b" 
secret = "e62e170ab8644ded95cdb767d129a3f7"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

for i in range(0,10000,50):
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
        
        

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data


client_id = {"60c2edd789ef42c5ae87e2b5ad4a6d4b"}
client_secret = {"e62e170ab8644ded95cdb767d129a3f7"}
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API
name = "{Artist Name}" #chosen artist
result = sp.search(name) #search query
result['tracks']['items'][0]['artists']       
        


