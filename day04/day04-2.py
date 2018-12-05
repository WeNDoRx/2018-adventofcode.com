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

agents_log = {}
for key in sorted(d.iterkeys()):
	agent = d[key][0]
	
	if not agent in agents_log:
		agents_log[agent] = [0] * 60
	for minute in xrange(0, 60):
		if d[key][1][minute] == "#":
			agents_log[agent][minute] += 1

maxi = 0
minu = 0
agentm = 0
for agent, minutes in agents_log.iteritems():
	for minute in xrange(0, 60):
		if minutes[minute] > maxi:
			maxi = minutes[minute]
			minu = minute
			agentm = agent


print int(agentm)*minu