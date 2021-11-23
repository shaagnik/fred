#!/usr/bin/env python

from music21 import *
from generator import *
from weights import *
from genetics import *
from weightedrandomizer import *

gen = gen_generation([], 10)

print('generation 0')
print(gen[0])
gen[0][0].play()

i=0
while i < 100:
	print('generation ' + str(i+1))
	newGen = gen_generation(gen, 100)
	print(newGen[0])
	newGen[0][0].play()
	del gen[:]
	gen = newGen
	del newGen[:]
	i+=1

quit()