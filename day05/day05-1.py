#!/usr/bin/env python

# this is not optimised since I don't have time right now to think of a better algorithm than the stupid head-first-retarded-bruteforce-using-god-damn-strings

with open("input","r") as f:
	polymers = f.read().splitlines()

def remove_first_clashing(polymer):
	x = 0
	while x < len(polymer) - 1:
		# if they are the same and different case
		if polymer[x].lower() == polymer[x+1].lower() and polymer[x].islower() != polymer[x+1].islower():
			return polymer[:x] + polymer[x+2:]
		x += 1
	return polymer

def remove_all_clashing(polymer):
	while polymer != remove_first_clashing(polymer):
		polymer = remove_first_clashing(polymer)
	return polymer

for polymer in polymers:
	new_polymer = remove_all_clashing(polymer)
	print len(new_polymer)