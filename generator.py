#!/usr/bin/env python

from music21 import *
from random import randint

class Voice:
    def __init__(self):
        self.notes = []
    def setNotes(self, notes):
        self.notes = notes
    def play(self):
        x = stream.Stream(self.notes)
        s = midi.realtime.StreamPlayer(x)
        s.play()

def gen_voice(length, lowest, highest):
    tone_range = interval.Interval(lowest, highest)
    notes = []
    for l in range(0, length + 1):
        dist = randint(0, tone_range.cents/100)
        newNote = lowest.transpose(dist)
        notes.append(newNote)
    result = Voice()
    result.setNotes(notes)
    return result

class Piece:
    def __init__(self):
        self.voices = []
    def setVoices(self, voices):
        self.voices = voices
    def play(self):
        x = stream.Stream()
        for v in self.voices:
            y = stream.Part(v.notes)
            x.append(y)
        s = midi.realtime.StreamPlayer(x)
        s.play()
