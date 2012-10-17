#!/usr/bin/python2.7 -B

import fonts

'''
extract(string, string, int, int, int):

Extracts a script file from Crest of Gaia given a pointer table.
'''
def extract(filename, output, address, count, offset, end):
	# Open ROM for input
	f = open(filename, "rb")
	f.seek(address)
	idx_pointers = []

	# Read pointers to array
	for k in range(0, count):
		idx_pointers.append(ord(f.read(1)) + ord(f.read(1)) * 0x100 + \
			offset)
	idx_pointers.append(end)

	# Begin output
	o = open(output + ".txt", "w")
	for k in range(0, len(idx_pointers)-1):
		f.seek(idx_pointers[k])
		fnt_table = 0

		# Read from pointer start to next pointer
		while(f.tell() < idx_pointers[k + 1]):
			read_char = ord(f.read(1))

			# Toggle katakana/hiragana output after reading "*"
			if(read_char == 0x2a):
				fnt_table ^= 1
				continue

			# Write character from table
			if(fnt_table == 0):
				o.write(fonts.katakana[read_char])
			if(fnt_table == 1):
				o.write(fonts.hiragana[read_char])

			# Write visible line breaks
			if(read_char == 0x5c and f.tell() < idx_pointers[k + 1]):
				o.write("\n")
		o.write("<>\n\n")
	o.close()
	f.close()


'''
extract_fixed(string, string, list):

Extracts a script file from Crest of Gaia given a pointer table.
'''
def extract_fixed(filename, output, strings):
	# Open ROM for input
	f = open(filename, "rb")

	# Begin output
	o = open(output + ".txt", "w")

	for i in range(0, len(strings)):
		f.seek(strings[i][1])
		fnt_table = 0

		# Read from pointer start to next pointer
		while(f.tell() < strings[i][1] + strings[i][2]):
			read_char = ord(f.read(1))

			# Toggle katakana/hiragana output after reading "*"
			if(read_char == 0x2a):
				fnt_table ^= 1
				continue

			# Write character from table
			if(fnt_table == 0):
				o.write(fonts.katakana[read_char])
			if(fnt_table == 1):
				o.write(fonts.hiragana[read_char])

			# Write visible line breaks
			if(read_char == 0x5c and f.tell() != strings[i][1] + strings[i][2]):
				o.write("\n")
		o.write("<>\n\n")
	o.close()
	f.close()
