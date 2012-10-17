#!/usr/bin/python2.7 -B

# Initialize the program
try:
	import csv

except ImportError, err:
	print "Could not load %s module." % (err)
	raise SystemExit

def extract_units(rom, output):
	names = [
		"Light Lord",
		"Grand Dino",
		"Falcon Knight",
		"Light Knight",
		"Fighter",
		"Archer",
		"White Dragon",
		"Armor Knight",
		"Dragon Knight",
		"Crossbow",
		"Aqua Fighter",
		"Turtle Knight",
		"Aqua Knight",
		"Galley Ship",
		"Civilian",
		"Type-74 Tank",
		"Private",
		"AH-1 Cobra",
		"Jeep",
		"Foot Soldier",
		"Cavalry",
		"Gunman",
		"Shinobi",
		"Dark Lord",
		"Horn Dino",
		"Wing Knight",
		"Dark Knight",
		"Berserker",
		"Gunner Wolf",
		"Dark Dragon",
		"Dark Armor",
		"Wyvern",
		"Catapult",
		"Merman",
		"King Lobster",
		"Kraken",
		"Great Eel",
		"Zombie",
		"T-72 Tank",
		"Private",
		"MI-24 HIND",
		"Jeep",
		"Foot Soldier",
		"Cavalry",
		"Gunman",
		"Shinobi"
		]
	f = open(rom, "rb")
	table = []
	
	# Repeat for all 46 units
	for i in range(0, 46):
		f.seek(i * 4)
		unit = []

		# Name
		unit.append(names[i])
		# Attack, Range, Defense, Move
		for k in range(0, 4):
			unit.append(ord(f.read(1)))
		# Evasion
		f.seek(i + 0xb8)
		unit.append(ord(f.read(1)))
		# Type
		f.seek(i + 0xd2)
		unit.append(ord(f.read(1)))
		# Cost
		f.seek(i + 0x114)
		unit.append(ord(f.read(1)))
		table.append(unit)

	o = open(output, "wb")
	csv_table = csv.writer(o)

	# Write CSV header
	csv_table.writerow(["UNIT", "ATK", "RANGE", "DEF", "MOVE", "EVADE", "TYPE", "COST"])

	# Write CSV rows
	for i in range(0, 46):
		csv_table.writerow(table[i])
	o.close()


def extract_terrain(rom, output):
	f = open(rom, "rb")
	f.seek(0x280)

	# Terrain
	table = []
	for k in range(0, 10):
		table.append(ord(f.read(1)))

	o = open(output, "wb")
	csv_table = csv.writer(o)

	# Write CSV
	csv_table.writerow(["FIELD", "FOREST", "MOUNTAIN", "DESERT", "CASTLE", "WALL", "BRIDGE", "BOULDER", "WATER", "STATUE"])
	csv_table.writerow(table)

	o.close()

