# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:40:07 2019

@author: JamarcH_Temp
"""

import json
import requests
#from furl import furl
from math import ceil

# to save some typing
import pandas as pd
import matplotlib

# to display plots in the notebook

import matplotlib.pyplot as plt

TOKEN = "e62e170ab8644ded95cdb767d129a3f7"
url = "https://api.spotify.com/v1/me/tracks"
headers = {'Authorization': "Bearer {}".format(TOKEN)}
r = requests.get(url, headers=headers)
parsed = json.loads(r.text)

count_songs = parsed["total"]
print("Total number of songs: {}".format(count_songs))


# paginate over all tracks
all_songs = []
for i in range(int(ceil(count_songs/50.0))):
    offset = 50*i
    url = "https://api.spotify.com/v1/me/tracks?limit=50&offset={}".format(offset)
    headers = {'Authorization': "Bearer {}".format(TOKEN)}
    r = requests.get(url, headers=headers)
    parsed = json.loads(r.text)

    all_songs.extend(parsed["items"])
print("Number of gathered songs: {}".format(len(all_songs)))
