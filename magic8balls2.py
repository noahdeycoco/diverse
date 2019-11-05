# !/usr/bin/env python3
# *-* coding: utf-8

import random
sentences = ['This is the first.',
'This is the last.',
'Who knows?',
'Right above you !',
'I don\'t believe it!',
'Not now...']

phrase = sentences[random.randint(0, (len(sentences)-1))]
print(str(sentences.index(phrase))+': '+phrase)


