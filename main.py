#!/usr/bin/env python

from music21 import *
from genetics import *
from weights import *

def get_top(list):
	top = [None, 0]
	for value, weight in list:
		if(weight > top[1]):
			top = [value, weight]
	return top

gen = gen_generation([], generation_size)

print('generation 0')
top = get_top(gen)
top[0].play()


i = 0
old_score = top[1]
streak = 0
while i < num_generations:
	print('generation ' + str(i+1))
	new_gen = gen_generation(gen, generation_size)
	if(i%100 == 0):
		top = get_top(new_gen)
		print(top[1], top[1] - old_score, streak)
		if(top[1] - old_score > 0):
			streak+= 1
		else:
			streak = 0
		old_score = top[1]
		top[0].write('top.mid')
	del gen[:]
	gen = new_gen
	i += 1
top = get_top(gen)
print(top)
top[0].write('top.mid')
top[0].play()
quit()