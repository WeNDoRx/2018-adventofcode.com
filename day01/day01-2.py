#!/usr/bin/env python

f = open("input","r")

freq, i, v, found = 0, 0, [0], False

while not found:
	f.seek(0)
	for line in f:
		n = int(line.replace("\n", ""))
		freq = freq+n
		if freq in v:
			print freq
			found = True
			break
		v.append(freq)