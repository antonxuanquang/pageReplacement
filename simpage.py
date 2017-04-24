import fileinput
import sys
from fifo import page_fault as fifo

def page_fault(algorithm, pages, frames):
	if algorithm == "FIFO":
		return fifo(pages, frames)
	elif algorithm == "LRU":
		return 20000
	elif algorithm == "LFU":
		return 30000
	elif algorithm == "OPT":
		return 40000
	elif algorithm == "RAND":
		return 50000
	elif algorithm == "MFU":
		return 60000
	elif algorithm == "MRU":
		return 70000
	else:
		return -1

# read everything from files and put it into an array
input = []
for line in fileinput.input():
	input.append(line.strip())

# parse 1st and 2nd lines. If can't, prompt error 
# and terminate program
try: 
	pages = [int(x) for x in input[0].split(' ')]
	frames = int(input[1])
	print "Page Reference String: %s" % input[0]
	print "Number of Frames: %s" % input[1]
except ValueError:
	print "Invalid input. Program exit"
	sys.exit()

for line in input[2:]:
	faults = page_fault(line, pages, frames)
	if faults >= 0:
		print "%s: %d" % (line, faults)
	else:
		print "Invalid algorithm name. Program exit"
		sys.exit()