def page_fault(pages, frames):

	if frames >= len(pages):
		return len(pages)

	memory = []
	page_faults = 0

	for page in pages:
		# if not in memory, remove the first page
		if page not in memory:
			# remove a page only if memory is filled up
			if len(memory) == frames:
				del memory[0]
			page_faults = page_faults + 1

		# if in memory, remove the page from memory
		else:
			index = memory.index(page)
			del memory[index]

		# always add new page at the beginning of memory stack
		memory.insert(0, page)
 
	return page_faults