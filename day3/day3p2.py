#!/usr/bin/python2.7

from collections import defaultdict
map = defaultdict(int)
unique_houses = 1
filename = "day3_input"

x_coord_santa = 0
y_coord_santa = 0

x_coord_robosanta = 0
y_coord_robosanta = 0

map[x_coord_santa, y_coord_santa] += 1

num = 0

def new_location(map, x, y, houses):
	map[x, y] += 1
	if map[x, y] == 1:
		houses += 1
	return (map, x, y, houses)

with open(filename) as f:
	while True:
		c = f.read(1)
		if not c:
			break
		if c == "^":
			if num % 2 == 0:
				y_coord_santa += 1
				(map, x_coord_santa, y_coord_santa, unique_houses) = new_location(map, x_coord_santa, y_coord_santa, unique_houses)
			else:
				y_coord_robosanta += 1
				(map, x_coord_robosanta, y_coord_robosanta, unique_houses) = new_location(map, x_coord_robosanta, y_coord_robosanta, unique_houses)
		elif c == "v":
			if num % 2 == 0:
				y_coord_santa -= 1
				(map, x_coord_santa, y_coord_santa, unique_houses) = new_location(map, x_coord_santa, y_coord_santa, unique_houses)
			else:
				y_coord_robosanta -= 1
				(map, x_coord_robosanta, y_coord_robosanta, unique_houses) = new_location(map, x_coord_robosanta, y_coord_robosanta, unique_houses)
		elif c == ">":
			if num % 2 == 0:
				x_coord_santa += 1
				(map, x_coord_santa, y_coord_santa, unique_houses) = new_location(map, x_coord_santa, y_coord_santa, unique_houses)
			else:
				x_coord_robosanta += 1
				(map, x_coord_robosanta, y_coord_robosanta, unique_houses) = new_location(map, x_coord_robosanta, y_coord_robosanta, unique_houses)
		elif c == "<":
			if num % 2 == 0:
				x_coord_santa -= 1
				(map, x_coord_santa, y_coord_santa, unique_houses) = new_location(map, x_coord_santa, y_coord_santa, unique_houses)
			else:
				x_coord_robosanta -= 1
				(map, x_coord_robosanta, y_coord_robosanta, unique_houses) = new_location(map, x_coord_robosanta, y_coord_robosanta, unique_houses)
		num += 1

print unique_houses
