#!/usr/bin/python2.7 -B

'''
background(string, int, int, int, array):

Generates a mosaic definition for a PC-Engine background at the given offset.
'''
def background(output, width, height, offset, pal):
	o = open(output, "w")
	o.write("offset: 8 * " + hex(offset) + "\n")
	o.write("width: " + str(width) + "\n")
	o.write("height: " + str(height) + "\n")
	o.write("\n")
	o.write("depth: 4\n")
	o.write("palette: " + hex(pal[0x0]) + ", " + hex(pal[0x1]) + ", " + hex(pal[0x2]) + ", " + hex(pal[0x3]) + "\n")
	o.write("palette: " + hex(pal[0x4]) + ", " + hex(pal[0x5]) + ", " + hex(pal[0x6]) + ", " + hex(pal[0x7]) + "\n")
	o.write("palette: " + hex(pal[0x8]) + ", " + hex(pal[0x9]) + ", " + hex(pal[0xa]) + ", " + hex(pal[0xb]) + "\n")
	o.write("palette: " + hex(pal[0xc]) + ", " + hex(pal[0xd]) + ", " + hex(pal[0xe]) + ", " + hex(pal[0xf]) + "\n")
	o.write("\n")
	o.write("block: f(8,0,4)   0 + n\n")
	o.write("block: f(8,1,4)   8 + n\n")
	o.write("block: f(8,2,4) 128 + n\n")
	o.write("block: f(8,3,4) 136 + n\n")
	o.write("\n")
	o.write("blockWidth: 8\n")
	o.write("blockHeight: 1\n")
	o.write("blockStride: 16\n")
	o.write("\n")
	o.write("tileWidth: 1\n")
	o.write("tileHeight: 8\n")
	o.write("tileStride: 128\n")
	o.close()


'''
sprite(string, int, int, int, array):

Generates a mosaic definition for a PC-Engine sprite at the given offset.
'''
def sprite(output, width, height, offset, pal):
	o = open(output, "w")
	o.write("offset: 8 * " + hex(offset) + "\n")
	o.write("width: " + str(width) + "\n")
	o.write("height: " + str(height) + "\n")
	o.write("\n")
	o.write("depth: 4\n")
	o.write("palette: " + hex(pal[0x0]) + ", " + hex(pal[0x1]) + ", " + hex(pal[0x2]) + ", " + hex(pal[0x3]) + "\n")
	o.write("palette: " + hex(pal[0x4]) + ", " + hex(pal[0x5]) + ", " + hex(pal[0x6]) + ", " + hex(pal[0x7]) + "\n")
	o.write("palette: " + hex(pal[0x8]) + ", " + hex(pal[0x9]) + ", " + hex(pal[0xa]) + ", " + hex(pal[0xb]) + "\n")
	o.write("palette: " + hex(pal[0xc]) + ", " + hex(pal[0xd]) + ", " + hex(pal[0xe]) + ", " + hex(pal[0xf]) + "\n")
	o.write("\n")
	o.write("block: f(16,0,4)   0 + n ^ 8\n")
	o.write("block: f(16,1,4) 256 + n ^ 8\n")
	o.write("block: f(16,2,4) 512 + n ^ 8\n")
	o.write("block: f(16,3,4) 768 + n ^ 8\n")
	o.write("\n")
	o.write("blockWidth: 16\n")
	o.write("blockHeight: 1\n")
	o.write("blockStride: 16\n")
	o.write("\n")
	o.write("tileWidth: 1\n")
	o.write("tileHeight: 16\n")
	o.write("tileStride: 1024 - 256")
	o.close()


