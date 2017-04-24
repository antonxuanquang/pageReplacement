def page_fault(pages, frames):
	memory = []
	page_faults = 0
	
	# fill up memory with pages
	for i in range(0, frames):
		if i == len(pages):
			return page_faults
		else:
			memory.append(pages[i])
			page_faults = page_faults + 1
	
	for page in pages[frames:]:
		# if not in memory, pop the first one, append new page 
		# to memory
		if page not in memory:
			del memory[0]
			memory.append(page)
			page_faults = page_faults + 1

	return page_faults