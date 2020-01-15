# -*- coding: utf-8 -*-
"""
Created on Tue May  7 08:33:36 2019

@author: JamarcH_Temp
"""

import nltk.chat

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}

chat = Chat(pairs,my_dummy_reflections)

print my_dummy_reflections
