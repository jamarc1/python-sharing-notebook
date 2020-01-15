# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:45:04 2019

@author: Jamarc.Hurd
"""

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#url = 'https://web.mta.info/developers/turnstile.html'
url = 'https://www.georgiapublicnotice.com'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

soup.findAll('a')

for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links

    one_a_tag = soup.findAll('a')[i]

    link = one_a_tag['href']

    download_url = 'http://web.mta.info/developers/'+ link

    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 

    time.sleep(1) #pause the code for a sec