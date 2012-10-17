#!/usr/bin/python2.7 -B

'''
###############################################################################

BEGIN CONFIGURATION
'''

input_rom     = "gaia.pce.bak"

# UNIX
mosaic_path   = "/home/d/.local/bin/mosaic"
# Windows
#mosaic_path  = "C:\\PROGRA~1\\BIN\\MOSAIC.EXE"

'''
END CONFIGURATION

###############################################################################
'''


# Initialize the program
try:
	import tarfile
	from os import system
	from struct import unpack
	from include import mosaic
	from include import shared
	from include import script
	from include import tables
	from include import maps

except ImportError, err:
        print "Could not load %s module." % (err)
        raise SystemExit


# Copyright notice
print "Crest of Gaia Toolchain 0.1 (cli)"
print "Copyright (c) 2012 Derrick Sobodash\n"

# Make sure all the output folders exist so we have no errors
shared.ensure_dir("./resources")
shared.ensure_dir("./resources/graphics")
shared.ensure_dir("./resources/maps")
shared.ensure_dir("./resources/mosaic")
shared.ensure_dir("./resources/scripts")


'''
###############################################################################

EXTRACT PC-ENGINE PALETTES
'''

print "Reading palettes..."

bgrpal = shared.read_pce_pal(input_rom, 0x69e)
sprpal = shared.read_pce_pal(input_rom, 0x89e)

print "Writing palettes..."

# Generate a python script with all game palettes
o = open("./resources/palettes.py", "w")

o.write("#!/usr/bin/python2.7 -B\n\n")
o.write("'''\n")
o.write("Changes in this file are applied to the ROM during next build.\n")
o.write("'''\n\n")
o.write("sprite = [\n")

# Print palette lists to file
for i in range(0, len(sprpal)):
	o.write("	# Palette " + str(i) + "\n	[\n	")
	for k in range(0, len(sprpal[i])):
		o.write(hex(sprpal[i][k]) + ", ")
		if((k + 1) % 4 == 0):
			o.write("\n	")
	o.write("],\n")
o.write("]\n\n")

o.write("background = [\n")
for i in range(0, len(bgrpal)):
	o.write("	# Palette " + str(i) + "\n	[\n	")
	for k in range(0, len(bgrpal[i])):
		o.write(hex(bgrpal[i][k]) + ", ")
		if((k + 1) % 4 == 0):
			o.write("\n	")
	o.write("],\n")
o.write("]\n\n")

# Write the Python header so we can include it later
o = open("./resources/__init__.py", "w")
o.close()

'''
###############################################################################

GENERATE MOSAIC FILES
'''

# Graphics in PC-Engine Sprite (16x16) format
tbl_sprite = [
	# Filename               Col Row   Offset  Palette
	["sprites-light1",        23,  1,  0xe000, sprpal[0x0]],
	["sprites-dark1",         23,  1,  0xeb80, sprpal[0x1]],
	["sprites-crests",         4,  1,  0xf700, sprpal[0x4]],
	["sprites-explosion",      5,  1,  0xf900, sprpal[0x0]],
	["sprites-unknown",        5,  1,  0xfb80, sprpal[0x0]],
	["sprites-combat",         2,  1,  0xfe00, sprpal[0x0]],
	["sprites-light2",        23,  1, 0x18000, sprpal[0x0]],
	["sprites-dark2",         23,  1, 0x18b80, sprpal[0x1]],
	["sprites-lightcrest",     2,  2, 0x19800, sprpal[0x4]],
	["sprites-neutralcrest2",  2,  2, 0x19a00, sprpal[0x4]],
	["sprites-darkcrest",      2,  2, 0x19c00, sprpal[0x4]],
	["sprites-light3",        23,  1, 0x2a000, sprpal[0x0]],
	["sprites-dark3",         23,  1, 0x2ab80, sprpal[0x1]],
	["sprites-light4",        23,  1, 0x2c000, sprpal[0x0]],
	["sprites-dark4",         23,  1, 0x2cb80, sprpal[0x1]],
	["logo-ncs1",              2,  2, 0x2d800, sprpal[0xc]],
	["logo-ncs2",              2,  2, 0x2da00, sprpal[0xc]],
	["logo-ncs3",              2,  2, 0x2dc00, sprpal[0xc]],
	["sprites-light5",        23,  1, 0x2e000, sprpal[0x0]],
	["sprites-dark5",         23,  1, 0x2eb80, sprpal[0x1]],
	["title",                  2, 32, 0x30000, sprpal[0x5]]
]

# Graphics in PC-Engine Background (8x8) format
tbl_background = [
	# Filename               Col Row   Offset  Palette
	["font",                  16, 13,  0xc000, bgrpal[0x0]],
	["map1",                  16, 16, 0x12000, bgrpal[0x8]],
	["map2",                  16, 16, 0x14000, bgrpal[0x8]],
	["terrain",               16,  4, 0x16000, bgrpal[0x4]],
	["ending-light1",         16,  9, 0x20000, bgrpal[0x9]],
	["ending-light2",         16,  9, 0x21200, bgrpal[0x9]],
	["ending-dark1",          16,  9, 0x22400, bgrpal[0x9]],
	["ending-good1",          16,  8, 0x24000, bgrpal[0x9]],
	["ending-good2",          16,  8, 0x25000, bgrpal[0x9]],
	["ending-good3",          16,  8, 0x26000, bgrpal[0x9]],
	["ending-bad1",           16,  8, 0x27000, bgrpal[0x9]],
	["portrait1",             16,  8, 0x32000, bgrpal[0x9]],
	["portrait2",             16,  8, 0x33000, bgrpal[0x9]],
	["portrait3",             16,  8, 0x34000, bgrpal[0x9]],
	["portrait4",             16,  8, 0x35000, bgrpal[0x9]],
	["portrait5",             16,  8, 0x36000, bgrpal[0x9]],
	["portrait6",             16,  8, 0x37000, bgrpal[0x9]]
]


print "Generating Mosaic presets..."

for i in range(0, len(tbl_sprite)):
	mosaic.sprite("./resources/mosaic/" + tbl_sprite[i][0] + ".mosaic", \
		tbl_sprite[i][1], tbl_sprite[i][2], tbl_sprite[i][3], \
		tbl_sprite[i][4])

for i in range(0, len(tbl_background)):
	mosaic.background("./resources/mosaic/" + tbl_background[i][0] + \
		".mosaic", tbl_background[i][1], tbl_background[i][2], \
		tbl_background[i][3], tbl_background[i][4])


'''
###############################################################################

EXTRACT GRAPHICS TO BITMAPS
'''

print "Extracting graphics..."

for i in range(0, len(tbl_sprite)):
	system(mosaic_path + " -export ./resources/mosaic/" + \
		tbl_sprite[i][0] + ".mosaic " + input_rom + \
		" ./resources/graphics/" + tbl_sprite[i][0] + ".bmp")

for i in range(0, len(tbl_background)):
	system(mosaic_path + " -export ./resources/mosaic/" + \
		tbl_background[i][0] + ".mosaic " + input_rom + \
		" ./resources/graphics/" + tbl_background[i][0] + ".bmp")


'''
###############################################################################

EXTRACT SCRIPT
'''

# Add known pointer tables to the list
tbl_pointers = [
	# Filename    Pointers  ##  Offset   End
	["units",        0xa9e, 94, -0xe000,  0x13fa],
	["magic",       0xa4f0, 32,  0x6000,  0xa650],
	["magic-desc",  0xa650, 16,  0x6000,  0xad48],
	["locations",   0xad84, 60,  0x6000,  0xafdc],
	["scenario",    0xb076, 60,  0x6000,  0xb3aa],
	["endings",    0x1071f,  7,  0xc000, 0x10b7e],
	["prologues1", 0x1a000, 10, 0x16000, 0x1b8be],
	["prologues2", 0x1c000, 10, 0x18000, 0x1d99c],
	["prologues3", 0x1e000, 10, 0x1a000, 0x1fa49]
]

tbl_fixed = [ #a496
	["menu1",       0x3da7, 44],
	["point",       0xa496,  6],
	["unit",        0xa49c, 14],
	["a-",          0xa4aa,  3],
	["d-",          0xa4ad,  3],
	["r-",          0xa4b0,  3],
	["m-",          0xa4b3,  3],
	["light",       0xa4da, 12],
	["dark",        0xa4e6, 10],
	["opt-terrain", 0xaffa, 10],
	["neutral",     0xb010, 16],
	["opt-side",    0xb024, 22],
	["opt-scen1",   0xb3b9, 36],
	["opt-scen2",   0xb3dd, 11],
	["magic",       0xb4e8,  9],
	["max turn",    0xb4f9, 18],
	["max turn2",   0xb50b, 12],
	["misc",        0xb814, 33],
	["unk1",       0x10000, 43],
	["unk2",       0x1002b, 20],
	["unk3",       0x1003f, 20],
	["unk4",       0x10053, 10],
	["unk5",       0x1005d, 20],
	["unk6",       0x10071, 14],
	["unk7",       0x1008f, 60],
	["unk8",       0x100cb, 58],
	["light",      0x10105, 12],
	["dark",       0x10111, 10],
	["human-cpu",  0x1011b, 18],
	["pad",        0x1012d, 52],
	["yes-no",     0x10173, 65],
	["yes",        0x101b4,  8],
	["no",         0x101bc,  6],
	["no",         0x101bc,  6],
	["password1",  0x101c2, 61],
	["password2",  0x101ff, 21],
	["password3",  0x10214, 40],
	["initative",  0x1024a, 51],
	["light",      0x1027d, 12],
	["newgame",    0x1028f, 27],
	["push-i",     0x10718,  7],
	["password",   0x10b7e, 14],
	["light-dark", 0x10b8c, 14],
	["vs",         0x10b9a,  3],
        ["turn-point", 0x10b9d, 10],
	["menu2",      0x1128c, 49],
	["menu3",      0x112d7, 42],
	["presented",  0x1131d, 13],
]


print "Extracting text..."

for i in range(0, len(tbl_pointers)):
	print "  Dumping " + tbl_pointers[i][0] + "..."

	script.extract(input_rom, "./resources/scripts/" + tbl_pointers[i][0], \
		tbl_pointers[i][1], tbl_pointers[i][2], tbl_pointers[i][3], \
		tbl_pointers[i][4])

script.extract_fixed(input_rom, "./resources/scripts/fixed", tbl_fixed)


'''
###############################################################################

EXTRACT TABLES
'''

print "Extracting data tables..."

tables.extract_units(input_rom, "./resources/units.csv")
tables.extract_terrain(input_rom, "./resources/terrain.csv")


'''
###############################################################################

EXTRACT MAPS
'''

print "Extracting data tables..."

maps.extract(input_rom, "./resources/maps/")


'''
###############################################################################

CREATE BACKUP TARBALL
'''

print "Compressing resources to backup..."

import tarfile
tar = tarfile.open("./backup.tar.gz", "w|gz")
tar.add("./resources")
tar.close()


'''
###############################################################################

POST-PRODUCTION
'''

print "All resources successfully extracted!\n"
print "You can now make a copy of the resources folder to suit your whatever"
print "project you have in mind. A backup of its original state can be found"
print "in ./backup.tar.gz, just in case something goes wrong!"
