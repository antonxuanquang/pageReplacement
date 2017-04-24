import fileinput
import sys
from fifo import page_fault as fifo
from lru import page_fault as lru
from lfu import page_fault as lfu
from opt import page_fault as opt
from rand import page_fault as rand
from mfu import page_fault as mfu
from mru import page_fault as mru

def page_fault(algorithm, pages, frames, results):
	if algorithm not in results:
		if algorithm == "FIFO":
			results[algorithm] = fifo(pages, frames)
		elif algorithm == "LRU":
			results[algorithm] = lru(pages, frames)
		elif algorithm == "LFU":
			results[algorithm] = lfu(pages, frames)
		elif algorithm == "OPT":
			results[algorithm] = opt(pages, frames)
		elif algorithm == "RAND":
			results[algorithm] = rand(pages, frames)
		elif algorithm == "MFU":
			results[algorithm] = mfu(pages, frames)
		elif algorithm == "MRU":
			results[algorithm] = mru(pages, frames)
		else:
			return -1
	return results[algorithm]

# read everything from files and put it into an array
input = []
for line in fileinput.input():
	input.append(line.strip())
results = {}
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
	line = line.upper().strip()
	if not line:
		continue
	faults = page_fault(line, pages, frames, results)
	if faults >= 0:
		print "%s: %d" % (line, faults)
	else:
		print "Invalid algorithm name. Program exit"
		sys.exit()