def page_fault(pages, frames):

	if frames >= len(pages):
		return len(pages)

	memory = []
	page_faults = 0
	timeline_map = {}

	for i in range(0, len(pages)):
		timeline = timeline_map.get(pages[i], [])
		timeline.append(i)
		timeline_map[pages[i]] = timeline

	for page in pages:
		# if not in memory, remove the last one
		if page not in memory:
			# remove a page only if memory is filled up
			if len(memory) == frames:
				del memory[-1]
			page_faults = page_faults + 1

		# if in memory, remove the page from memory
		else:
			index = memory.index(page)
			del memory[index]

		# update timeline map: remove the first element in the 
		# list that map to page
		timeline = timeline_map.get(page)
		del timeline[0]
		timeline_map[page] = timeline


		# add the new page in a way such that the nearest page 
		# about to be used is always at the top of the stack.
		if timeline_map.get(page):
			index = 0
			time = timeline_map.get(page)[0]
			while index < len(memory):
				if memory:
					timeline = timeline_map.get(memory[index])
					if timeline and time > timeline[0]:
						index = index + 1
					else:
						break	
				else:
					break
		# if a page is not going to be used in the future, assume that
		# it is used after every pages
		else:
			index = len(memory)
		
		memory.insert(index, page)
		
 
	return page_faults