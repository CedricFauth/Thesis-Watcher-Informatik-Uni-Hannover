class SiteEntries:
	class entry:
		def __init__(self) -> None:
			self.title = None
			self.thtype = None
			self.others = []
	
	def __init__(self) -> None:
		self.entries = []
	
	def add(self, title, thtype, others=None) -> None:
		'''Adds a new entry to the entries
		title: Title of Thesis
		thtype: Type of Thesis (can be arbitrary string)
		others: UNUSED AT THE MOMENT! (list of additional information)
		'''
		e = self.entry()
		e.title = title
		e.thtype = thtype
		if others:
			e.others = others
		self.entries.append(e)
	
	def __str__(self) -> str:
		out = ""
		i = 0
		for e in self.entries:
			second = None
			l = 80 - len(e.thtype) - 9
			if len(e.title) > l:
				out += '{:>2}. {} [{}]'.format(i, e.title[:l+1], e.thtype)
				out += '\n    {}'.format(e.title[l+1:])
			else:
				out += '{:>2}. {:<{len}} [{}]'.format(i, e.title, e.thtype, len=l+1)

			#if (len(e.others)):
			#	out += "\tmore: " + str(e.others)
			i += 1
			out += '\n'
		return out
	