#!/usr/bin/env python
from generator import *
from weights import *
from weightedrandomizer import *

def first_gen(size):
	result = []
	i = 0
	print('generating')
	while i < size:
		p = gen_piece(piece_length, 
			[[note.Note('c1'), note.Note('c2')],
			[note.Note('c3'),note.Note('c4')],
			[note.Note('c5'),note.Note('c6')],
			[note.Note('c7'),note.Note('c8')]])
		result.append([p, score_piece(p)])
		print('.', end='')
		i += 1
	return result

def gen_generation(previousGen, size):
	parents = previousGen
	if(len(previousGen) == 0):
		parents = first_gen(size)
	i = 0
	result = []
	wr = WeightedRandomizer(parents)
	print('generating children')
	while i < size:
		child = mate(wr.random()[0], wr.random()[0])
		result.append([child, score_piece(child)])
		print('.',end='')
		i += 1
	return result
