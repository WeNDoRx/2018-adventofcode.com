#!/usr/bin/env python

import numpy as np

f = open("input","r")

a = np.zeros((1000, 1000))
d = {}

for line in f:
	claim = line.replace("\n", "")
	at_split = claim.split("@")
	claim_id = int(at_split[0][1:-1])
	d[claim_id] = True
	colon_split = at_split[1].split(":")
	comma_split = colon_split[0].split(",")
	x_split = colon_split[1].split("x")
	left_padding = int(comma_split[0])
	top_padding = int(comma_split[1])
	width = int(x_split[0])
	heigth = int(x_split[1])
	for x in xrange(left_padding, left_padding + width):
		for y in xrange(top_padding, top_padding + heigth):
			if a[y][x] != 0:
				d[a[y][x]] = False
				d[claim_id] = False
			a[y][x] = claim_id

for key, value in d.iteritems() :
    if value == True:
    	print key