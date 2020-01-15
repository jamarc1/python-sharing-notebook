# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:18:38 2019

@author: JamarcH_Temp
"""

import requests
from bs4 import BeautifulSoup


page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')

last_links = soup.find(class_ ='AlphaNav')
last_links.decompose()

player_list = soup.find(class_='BodyText')

player_list_items = player_list.find_all('a href')

for player_list in player_list_items:
    print(player_list.prettify())
    

