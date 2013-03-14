#!/usr/bin/env python

from music21 import *

g = [2,-10,1,-10,4,1,-10,4,-10,1,-10,1,2]

def get_interval_weight(i):
    index = ((int)(i.cents/100))%12
    return g[index]


