def page_fault(pages, frames):

	if frames >= len(pages):
		return len(pages)

	memory = []
	page_faults = 0
	frequency_map = {}

	for i in range(0, len(pages)):
		page = pages[i]
		# if not in memory, remove the last one
		if page not in memory:
			# remove a page only if memory is filled up
			if len(memory) == frames:
				key = memory[-1]
				del memory[-1]
				del frequency_map[key]
			page_faults = page_faults + 1

		# if in memory, remove the page from memory
		else:
			index = memory.index(page)
			del memory[index]

		# update frequency map
		node = frequency_map.get(page, [0, i])
		node[0] = node[0] + 1
		frequency_map[page] = node

		# add the new page in a way such that the memory stack 
		# keeps the most frequently used page at the top of stack.
		# The stack should also keep the FIFO order as well
		index = 0
		while index < len(memory):
			if (frequency_map.get(memory[index])[0] > frequency_map.get(page)[0]):
				index = index + 1
			elif (frequency_map.get(memory[index])[0] == frequency_map.get(page)[0]):
				if (frequency_map.get(memory[index])[1] < frequency_map.get(page)[1]):
					break
				index = index + 1
			else:	
				break
		
		memory.insert(index, page)
	return page_faults