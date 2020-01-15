# -*- coding: utf-8 -*-
"""
Created on Tue May  7 08:37:07 2019

@author: JamarcH_Temp
"""

from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Wassup %1, How are you today ?",]
    ],
     [
        r"what's your name?",
        ["My name is Marc and I'm a chatbot!",]
    ],
    [
        r"how are you ?",
        ["I'm Awesome\nHow about Yourself ?",]
    ],
    [
        r"I'm leaving ?",
        ["Cool, Be Safe!",]
    ],
    [
        r"sorry (.*)",
        ["Its cool","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello|wassup|waddup",
        ["Wassup","Hello", "Hey there"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program sir\nSeriously you are asking me this?",]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]

    ],
    [
        r"(.*) created ?",
        ["Lucky Lefty created me using some computer code in Python ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Atlanta, Georgia, it Influences Everything lol',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Super Cool company, I have heard about it. they are really winning these days.",]
    ]

]

def chatty():
    print("Hi, I'm Marc a chatbot and I talk alot ;)\nPlease type lowercase English language if you wanna talk. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()