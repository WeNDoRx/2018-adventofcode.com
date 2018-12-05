#!/usr/bin/env python

import string
from sys import exit

def diff_letters(a,b):
    return sum ( a[i] != b[i] for i in range(len(a)) )

def print_common(a, b):
	common = []
	for x in xrange(0, len(a)):
		if a[x] == b[x]:
			common.append(a[x])
	print "".join(common)

with open("input") as f:
	boxIDs = f.read().splitlines()
for a in boxIDs:
	for b in boxIDs:
		if a == b:
			continue
		if diff_letters(a,b) == 1:
			print_common(a,b)
			exit()