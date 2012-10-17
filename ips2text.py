#!/usr/bin/python2.7

# Initialize the program
try:
        import sys
        import glob
        import os
        import re
        from struct import *
        import time
        from stat import *

except ImportError, err:
        print "Could not load %s module." % (err)
        raise SystemExit

#convert string to hex
def toHex(s):
	lst = []
	for ch in s:
		hv = hex(ord(ch)).replace('0x', '')
		if len(hv) == 1:
			hv = '0'+hv
		lst.append(hv)
	
	return reduce(lambda x,y:x+y, lst)#convert string to hex

def inrange(offset):
	if offset > 0xe000 and offset < 0x10000:
		return 1
	# Palettes
	elif offset > 0x69e and offset < 0xa9f:
		return 1
	elif offset > 0x18000 and offset < 0x1a000:
		return 1
	elif offset > 0x2a000 and offset < 0x32000:
		return 1
	elif offset > 0xc000 and offset < 0xda00:
		return 1
	elif offset > 0x12000 and offset < 0x16a00:
		return 1
	elif offset > 0x20000 and offset < 0x28000:
		return 1
	
	elif offset > 0x30000 and offset < 0x38000:
		return 1
	elif offset > 0xb5a and offset < 0x13fa:
		return 1
	# Magic
	elif offset > 0xa4f0 and offset < 0xa650:
		return 1
	# Magic Desc
	elif offset > 0xa670 and offset < 0xad84:
		return 1
	# Loc
	elif offset > 0xad84 and offset < 0xafdc:
		return 1
	elif offset > 0xaffa and offset < 0xb03a:
		return 1
	elif offset > 0xb076 and offset < 0xb3e8:
		return 1
	elif offset > 0xb4e8 and offset < 0xb517:
		return 1
	elif offset > 0xb814 and offset < 0xb873:
		return 1
	elif offset > 0x10000 and offset < 0x102aa:
		return 1
	elif offset > 0x106ff and offset < 0x10ba8:
		return 1
	# Prologues
	elif offset > 0x1a000 and offset < 0x20000:
		return 1
	elif offset > 0xa9e and offset < 0x13fa:
		return 1
	return 0

def ips2txt(file):
	f = open(file, "rb")
	test = f.read(5)
	if test != "PATCH":
		print "Not an IPS file!"
		raise SystemExit
	rle = 0
	control = f.read(3)
	while control != "EOF":
		offset = unpack(">I", "\0" + control)
		size   = unpack(">H", f.read(2))
		if size[0] == 0:
			rle  = 1
			size = unpack(">H", f.read(2))
		bytes = ""
		#print size[0]
		#raise SystemExit
		if rle == 0:
			bytes = f.read(size[0])
		else:
			tempbyte = f.read(1)
			for i in range(0, size[0]):
				bytes += tempbyte
		if inrange(offset[0]) == 0:
	                print "----------------------------------------------------------------"
			print "Patched " + str(size[0]) + "bytes @ " + hex(offset[0] - 0x200) + "\n"
			print toHex(bytes) + "\n"
		rle = 0
		control = f.read(3)

file = sys.argv[1]

# Title Screen
ips2txt("crest.ips")
