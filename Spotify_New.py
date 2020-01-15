# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:43:24 2019

@author: Jamarc.Hurd
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

name = "{Drake}" #chosen Artist

result = sp.search(name)
result['tracks']['items'][0]['artists']


artist_uri = result['tracks']['items'][0]['artists'][0]['uri']

sp_albums = sp.artist_albums(artist_uri, album_type ='album')


album_names = []
album_uris = []
for i in range(len(sp_albums['items'])):
    album_names.append(sp_albums['items'][i]['name'])
    album_uris.append(sp_albums['items'][i]['uri'])
    
album_names
album_uris



def albumSongs(uri):
    album = uri #assign album uri to a_name
    
spotify_albums[album] = {} #Creates dictionary for that specific album
#Create keys-values of empty lists inside nested dictionary for album
    spotify_albums[album]['album'] = [] #create empty list
    spotify_albums[album]['track_number'] = []
    spotify_albums[album]['id'] = []
    spotify_albums[album]['name'] = []
    spotify_albums[album]['uri'] = []
    
tracks = sp.album_tracks(album) #pull data on album tracks

for n in range(len(tracks['items'])): #for each song track
        spotify_albums[album]['album'].append(album_names[album_count]) #append album name tracked via album_count
        spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
        spotify_albums[album]['id'].append(tracks['items'][n]['id'])
        spotify_albums[album]['name'].append(tracks['items'][n]['name'])
        spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])
        
        
        
        
        
        
        
        