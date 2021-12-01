#!/usr/bin/env python

from music21 import *
from random import randint, random
from weights import *
import copy

class Voice:
    def __init__(self, notes, note_range):
        self.notes = notes
        self.range = note_range
        self.stream = stream.Stream(notes)
    def get_note_at(self, position):
        result = (self.stream.iter().getElementsByOffset(position, mustBeginInSpan=False))
        return result.first()

    def get_half(self, first):
        pos = (int)(piece_length/2)
        if(first):
            return (self.stream.iter().getElementsByOffset(0,pos, mustBeginInSpan=False))
        else:
            return (self.stream.iter().getElementsByOffset(pos,pos*2, mustBeginInSpan=False))
    def play(self):
        s = midi.realtime.StreamPlayer(self.stream)
        s.play()
        del s


def gen_voice(length, lowest, highest):
    note_range = interval.Interval(noteStart=lowest, noteEnd=highest)
    notes = []
    i = 0
    while i < length:
        dist = randint(0, note_range.semitones+1)
        note_length = randint(0,4)
        if(dist == note_range.semitones):
            notes.append(note.Rest(quarterLength=note_length))
        else:
            new_note = lowest.transpose(dist)
            new_note.duration.quarterLength = note_length
            notes.append(new_note)
        i += note_length
    result = Voice(notes, note_range)
    return result

class Piece:
    def __init__(self, voices):
        self.voices = []
        self.length = 0
        self.voices = voices
        self.length = len(voices[0].notes)
    def play(self):
        x = stream.Stream()
        for v in self.voices:
            y = stream.Part(v.notes)
            x.append(y)
        s = midi.realtime.StreamPlayer(x)
        s.play()
        del s
        del x
    def write(self, filename):
        x = stream.Stream()
        for v in self.voices:
            y = stream.Part(v.notes)
            x.append(y)

        f = midi.translate.streamToMidiFile(x)
        f.open(filename, 'wb')
        f.write()
        f.close()

def gen_piece(length, ranges):
    voices = []
    for r in ranges:
        v = gen_voice(length,r[0],r[1])
        voices.append(v)
    return Piece(voices)

def mate(parent1, parent2):
    i = 0
    voices = []
    while i < min(len(parent1.voices), len(parent2.voices)):
        new_voice_notes = copy.deepcopy(list(parent1.voices[i].get_half(True))) + copy.deepcopy(list(parent2.voices[i].get_half(False)))
        new_voice = Voice(new_voice_notes, parent1.voices[i].range)
        voices.append(new_voice)
        i += 1
    child = Piece(voices)
    for v in child.voices:
        for n in v.notes:
            if((random() <= mutation_chance) & (not n.isRest)):
                if(n.isRest):
                    n = note.Note(v.range.noteStart)
                else:
                    dist = randint(-2, 2)
                    if(((n.pitch.ps + dist) <= v.range.noteEnd.pitch.ps) & ((n.pitch.ps + dist) >= v.range.noteStart.pitch.ps)):
                        n.pitch.ps += dist
    return child

