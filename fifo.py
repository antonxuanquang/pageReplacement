def page_fault(pages, frames):

	if frames >= len(pages):
		return len(pages)

	memory = []
	page_faults = 0
		
	for page in pages:
		# if not in memory, pop the first one, append new page 
		# to memory
		if page not in memory:
			# remove a page only if memory is filled up
			if len(memory) == frames:
				del memory[0]
			memory.append(page)
			page_faults = page_faults + 1

	return page_faults