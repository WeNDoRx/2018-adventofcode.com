#!/usr/bin/env python

import string

f = open("input","r")

two, three = 0, 0

for line in f:
	double = False
	tripple = False
	boxID = line.replace("\n", "")
	for char in string.ascii_lowercase:
		if boxID.count(char) == 2:
			double = True
		if boxID.count(char) == 3:
			tripple = True
	if double:
		two += 1
	if tripple:
		three += 1

print two * three