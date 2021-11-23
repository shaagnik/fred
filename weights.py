#!/usr/bin/env python

from music21 import *
from generator import *

g = [2,-.10,.1,-.10,4,.1,-.10,4,-.10,.1,-.10,.1,2]

mutation_chance = .01

piece_length = 4


measure_weight = [.1,.1,.1,.1]
position_weight = [.1,.1,.1,.1]

rhythm_melody_ratio = 1

duration_scores = [.1,.1,.1,.1]

# unison, min2nd, 2nd, min3rd, maj3rd, 4th, tritone, 5th, min6th, maj6th, min7th, maj7th, octave, rest
vertical_intervals = [0,0,0,0,.1,0,0,.1,0,0,.1,.1,.1]
horizontal_intervals = [.1,0,.1,0,.1,.1,0,.1,0,.1,0,.1,.1]
rest_weights = [.1,.1]

def get_interval_score(note1, note2, vertical):
    index = ((int)(note2.pitch.pitchClass - note1.pitch.pitchClass)) 
    if(vertical): 
        return vertical_intervals[index]
    return horizontal_intervals[index]

def get_positional_score(notes, position):
    # score for how many notes are starting and continuing, weighted by position
    return duration_scores[0]*position_weight[position]

def score_piece(piece):
    score = 0
    # horizontally score each voice
    for v in piece.voices:
        i = 0
        while i < len(v.notes)-1:
            score += get_interval_score(v.notes[i],v.notes[i+1],False) # times weight
            i += 1
    # vertically score each position
    # return weighted average
    return score

