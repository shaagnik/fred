#!/usr/bin/env python

from music21 import *

def play(stream):
    player = midi.realtime.StreamPlayer(stream)
    player.play()
