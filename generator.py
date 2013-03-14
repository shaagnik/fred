#!/usr/bin/env python

from music21 import *
from random import randint



def gen_voice(length, lowest, highest):
    result = stream.Stream()
    tone_range = interval.Interval(lowest, highest)
    for l in range(0, length + 1):
        dist = randint(0, tone_range.cents/100)
        x = lowest.transpose(dist)
        result.append(x)
    s = midi.realtime.StreamPlayer(result)
    s.play()
    return result

n = note.Note('c3')
n2 = note.Note('c4')
x = gen_voice(16, n, n2)

