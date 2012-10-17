#!/usr/bin/python2.7 -B

import Image, ImageDraw

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
			bits.append(str((current >> k) & 1))
	
	f.close()
	
	# Concatenate and return
	return(''.join(bits))


colors = [
	"#000000", "#000000", "#ffff00", "#db6d00",
	"#49ff6d", "#922400", "#ff4949", "#b624b6",
	"#4949ff", "#6d6dff", "#b6b6ff", "#006d24",
	"#00ff00", "#ff6dff", "#9292b6", "#ffffff"
	]

im = Image.new("RGBA", (16, 16))

gaia_rom = "gaia.pce.bak"

bits = bit_string(gaia_rom, 0xe000, 0x80)

print bits

draw = ImageDraw.Draw(im)
for i in range(0, 256):
	color = int(''.join([bits[i | 768], bits[i | 512],
						 bits[i + 256], bits[i]]), 2)
	draw.point((i % 16, i / 16), fill=colors[color])
del draw 

# write to stdout
im.save("test.png", "PNG")


