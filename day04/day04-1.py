#!/usr/bin/env python

d = {}

with open("input","r") as f:
	unsorted_log = f.read().splitlines()

log = sorted(unsorted_log)

guard = 0
start = 0
end   = 0
i = True

for line in log:
	split = line.split(" ")
	date = split[0][1:]
	time = split[1][3:5]

	if split[2] == "Guard":
		guard = split[3][1:]
		i = True
		continue

	if split[2] == "falls":
		if i:
			d[date] = [guard, "............................................................"]
			i = False
		start = int(time)
		continue
	
	if split[2] == "wakes":
		end = int(time)

		d[date][1] = d[date][1][:start] + "#" * (end - start) + d[date][1][end:]

#for key in sorted(d.iterkeys()):
# 	print key + '\t' + d[key][0] + '\t' + d[key][1]

total = {}

for key in sorted(d.iterkeys()):
	agent = d[key][0]
	slept = d[key][1].count("#")
	if not agent in total:
		total[agent] = slept
	else:
		total[agent] += slept

sleepyest_agent = max(total, key=total.get)
total[sleepyest_agent]

minutes = [0] * 60

for key in sorted(d.iterkeys()):
	if d[key][0] == sleepyest_agent:
	 	#print key + '\t' + d[key][0] + '\t' + d[key][1]
	 	for minute in xrange(0,60) :
	 		if d[key][1][minute] == "#":
	 			minutes[minute] += 1

max_index = max( range( len(minutes) ), key = lambda index : minutes[ index ] )
print max_index*int(sleepyest_agent)