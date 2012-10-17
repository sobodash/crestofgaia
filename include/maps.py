#!/usr/bin/python2.7 -B

def extract(file, output):
	offset = 0x28000
	f = open(file, "rb")
	terrain = [
		"G", "F", "M", "D", "C", "W", "B", "R", "S", "I"
		]

	for i in range(0, 30):
		f.seek(offset + i * 0x100)
		o = open(output + str(i + 1) + ".txt", "w")
		for i in range(0, 0x9a):
			o.write(terrain[ord(f.read(1))])
			if((i + 1) % 14 == 0 and i != 0):
				o.write("\n")
		o.close()
	f.close()
