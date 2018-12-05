#!/usr/bin/env python

import numpy as np

f = open("input","r")

a = np.zeros((1000, 1000))

for line in f:
	claim = line.replace("\n", "")
	at_split = claim.split("@")
	claim_id = int(at_split[0][1:-1])
	colon_split = at_split[1].split(":")
	comma_split = colon_split[0].split(",")
	x_split = colon_split[1].split("x")
	left_padding = int(comma_split[0])
	top_padding = int(comma_split[1])
	width = int(x_split[0])
	heigth = int(x_split[1])
	for x in xrange(left_padding, left_padding + width):
		for y in xrange(top_padding, top_padding + heigth):
			if a[y][x] == 0:
				a[y][x] = claim_id
			else:
				a[y][x] = "-1"

print (a == -1).sum()