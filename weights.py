#!/usr/bin/env python

from music21 import *
from generator import *


mutation_chance = .15

piece_length = 16
generation_size = 1000
num_generations = 5000


measure_weight = [.1,.1,.1,.1]
position_weight = [.1,.1,.1,.1]
duration_weight = [.1,.1,.1,.1]

voice_weight = [5, 2, 7, 1]
rhythm_melody_ratio = 1


# unison, min2nd, 2nd, min3rd, maj3rd, 4th, tritone, 5th, min6th, maj6th, min7th, maj7th, octave
vertical_intervals = [60,-100,-100,20,70,20,-150,80,0,0,0,60]
horizontal_intervals = [100,100,100,60,140,0,0,0,0,0,0,0]
rest_weight = [40,60]

def get_interval_score(note1, note2, vertical):
    if(note1 is not None and note2 is not None):
        if(note2.isRest | note1.isRest):
            return rest_weight[(0,1)[vertical]]
        index = ((int)(note2.pitch.pitchClass - note1.pitch.pitchClass))
        if(vertical): 
            return vertical_intervals[index%12]
        if(index>=12):
            return -100
        return horizontal_intervals[index]
    return 0

def get_positional_score(notes, position):
    # score for how many notes are starting and continuing, weighted by position
    return duration_weight[0]*position_weight[position]

def score_piece(piece):
    hscore = 0
    # horizontally score each voice
    for v in piece.voices:
        i = 0
        while i < len(v.notes)-1:
            hscore += (get_interval_score(v.notes[i],v.notes[i+1],False) * voice_weight[piece.voices.index(v)])
            i += 1
    # vertically score each position
    i = 0
    vscore = 0
    while i < piece_length:
        for v in piece.voices[1:]:
            vscore += get_interval_score(piece.voices[0].get_note_at(i),v.get_note_at(i),True)
        i += 1
    # return weighted average
    score = (hscore + (3 * vscore))/4
    if(score <= 0):
        score = 0.1
    return score

