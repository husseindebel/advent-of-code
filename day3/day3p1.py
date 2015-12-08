#!/usr/bin/python2.7

from collections import defaultdict
map = defaultdict(int)

unique_houses = 1
filename = "day3_input"

x_coord = 0
y_coord = 0
map[x_coord, y_coord] += 1

with open(filename) as f:
	while True:
		c = f.read(1)
		if not c:
			break
		if c == "^":
			y_coord += 1
			map[x_coord, y_coord] += 1
			if map[x_coord, y_coord] == 1:
				unique_houses += 1			
		elif c == "v":
			y_coord -= 1
			map[x_coord, y_coord] += 1
			if map[x_coord, y_coord] == 1:
				unique_houses += 1
		elif c == ">":
			x_coord += 1
			map[x_coord, y_coord] += 1
			if map[x_coord, y_coord] == 1:
				unique_houses += 1
		elif c == "<":
			x_coord -= 1
			map[x_coord, y_coord] += 1
			if map[x_coord, y_coord] == 1:
				unique_houses += 1
		
print unique_houses
