# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:22:40 2019

@author: Jamarc.Hurd
"""

import requests

request = requests.get('http://api.open-notify.org')
print(request.text)


people = requests.get('https://api.open-notify.org/astros.json')
print(people.text)

people_json = people.json()
print(people_json)