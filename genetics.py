#!/usr/bin/env python
from generator import *
from weights import *
from random import choices

def first_gen(size):
	result = []
	i = 0
	print('generating first gen')
	while i < size:
		p = gen_piece(piece_length, 
			[[note.Note('e2'), note.Note('e4')],
			[note.Note('b2'),note.Note('a4')],
			[note.Note('f3'),note.Note('e5')],
			[note.Note('c4'),note.Note('c6')]])
		result.append([p, score_piece(p)])
		i += 1
	return result

def sort_func(e):
	return e[1]

def gen_generation(previous_gen, size):
	parents = previous_gen
	if(len(previous_gen) == 0):
		parents = first_gen(size)
	i = 0
	result = []
	parents.sort(reverse=True, key=sort_func)
	# i = 0
	# while i < len(parents):
	# 	parents[i][1] /= (i+1)
	# 	i += 1

	random_parents = choices([item[0] for item in parents[0:((int)(size/4))]], [(int)(item[1]) for item in parents[0:((int)(size/4))]], k=2*size)
	
	while i+1 < size*2:
		if(random_parents[i] != random_parents[i+1]):
			child = mate(random_parents[i], random_parents[i+1])
			result.append([child, score_piece(child)])
		i += 2
	return result
