#!/usr/bin/env python

from music21 import *
from generator import *

x = gen_piece(4, [[note.Note('c1'),
	note.Note('c2')],
	[note.Note('c3'),note.Note('c4')],
	[note.Note('c5'),
		note.Note('c6')],[note.Note('c7'),note.Note('c8')]])
x.play()

y = gen_piece(4, [[note.Note('c1'),
	note.Note('c2')],
	[note.Note('c3'),note.Note('c4')],
	[note.Note('c5'),
		note.Note('c6')],[note.Note('c7'),note.Note('c8')]])
y.play()

(x.mate(y)).play()

quit()
