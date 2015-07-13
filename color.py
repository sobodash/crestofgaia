#!/usr/bin/python

'''
conv3to8(int):

Convert 9-bit PC-Engine color to 24-bit PC
'''
def conv3to8(color):
	# Isolate single colors from 9-bit GRB value
	g = color >> 6
	r = color >> 3 & 7
	b = color & 7
	# Expand 3-bit to 8-bit
	g = (g << 5) + (g << 2) + (g >> 1)
	r = (r << 5) + (r << 2) + (r >> 1)
	b = (b << 5) + (b << 2) + (b >> 1)
	# Merge to 24-bit RGB
	return(r * 0x10000 + g * 0x100 + b)

colors = [0x0, 0x38, 0xf8, 0x1f8,
	0xc7, 0x107, 0x197, 0x83,
	0x1ef, 0xa8, 0x178, 0x1fb,
	0x8a, 0x50, 0x124, 0x1ff
	]

for i in range(0, len(colors)):
	print hex(conv3to8(colors[i]))
