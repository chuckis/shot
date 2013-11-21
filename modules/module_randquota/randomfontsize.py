#!/usr/bin/python
# -*- coding: utf-8 -*-
# output is text with random font-size :)
#random quotation
#import os, sys
import __builtin__
import os
import sys
import threading
import traceback
from gluon import current
import random
filename = '/home/ruslan/yourtext.txt'

def read_words():
    with open(filename, 'r') as f:
        words = random.choice(f.readlines())
        words = words.decode('utf-8')
        f.close()
    return words
    
words = read_words()

def font_size():
    
    rand_size = random.randrange(10, 30)
    return rand_size
    
def getRandStyle():
    styled_text = []
    for word in words:
         word = u'<span style="font-size:' + str(font_size()) + 'px">' + word + '</span>'
         styled_text.append(word)
    return styled_text

random_font_text = " ".join(getRandStyle())


