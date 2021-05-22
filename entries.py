from colorama import Fore, Back, Style

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
		i = 1
		for e in self.entries:
			second = None
			l = 80 - len(e.thtype) - 8
			out += '{}{:>2}.{} '.format(Fore.MAGENTA, i, Fore.WHITE)
			if len(e.title) > l:
				out += '{} [{}]'.format(e.title[:l], e.thtype)
				out += '\n    {}'.format(e.title[l:])
			else:
				out += '{:<{len}} [{}]'.format(e.title, e.thtype, len=l)

			#if (len(e.others)):
			#	out += "\tmore: " + str(e.others)
			i += 1
			out += '\n'
		return out
