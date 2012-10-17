#!/usr/bin/python2.7 -B

# Initialize the program
try:
	import os
	import errno

except ImportError, err:
		print "Could not load %s module." % (err)
		raise SystemExit


'''
bit_string()

Returns the bits in a given string as a string. All data processing is based
on 16-bit little endian words.
'''
def bit_string(filename, offset, length):
	f = open(filename, "rb")
	f.seek(offset)
	
	# Use a list to store the bits since it will be faster in all
	# non-C Python implementations.
	bits = []
	
	while(f.tell() < (offset + length)):
		# Read a little endian word
		current = ord(f.read(1)) | ord(f.read(1)) << 8
		
		# Get each bit from most to least significant and add it to the list
		for k in range(15, -1, -1):
			bits.append(str(current >> k & 1))
	
	f.close()
	
	# Concatenate and return
	return(''.join(bits))


'''
color_to_24bit(int):

Convert 9-bit PC-Engine color to 24-bit PC
'''
def color_to_24bit(color):
	# Isolate single colors from 9-bit GRB value
	g = color >> 6
	r = color >> 3 & 7
	b = color & 7
	# Expand 3-bit to 8-bit
	g = g << 5 | g << 2 | g >> 1
	r = r << 5 | r << 2 | r >> 1
	b = b << 5 | b << 2 | b >> 1
	# Merge to 24-bit RGB
	return(r << 16 | g << 8 | b)


'''
color_to_9bit(int):

Convert 24-bit PC color to 9-bit PC-Engine
'''
def color_to_9bit(color):
	# Isolate colors from 24-bit RGB value and drop lower 5 bits
	r = (color >> 16) >> 5
	g = (color >> 8 & 0xff) >> 5
	b = (color & 0xff) >> 5
	# Merge to 9-bit GRB
	return(g << 6 | r << 3 | b)


'''
readpal(string, int):

Reads 16 palettes from PC-Engine game and spits them out in an array
'''
def read_pce_pal(file, offset):
	f = open(file, "rb")
	f.seek(offset)
	pal = []
	for i in range(0x0, 0x10):
		set = []
		for k in range(0x0, 0x10):
			set.append(color_to_24bit(ord(f.read(1)) | ord(f.read(1)) << 8))
		pal.append(set)
	return pal


'''
ensure_dir(string):

Check if a directory already exists and create it if it does not
'''
def ensure_dir(f):
	try:
		os.makedirs(f)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

