from random import randint

for i in xrange(100000):
	print randint(0,10),

print """
3
FIFO
LRU
LFU
OPT
RAND
MFU
"""