from entries import SiteEntries
from web import HTMLParser

def website_dbs() -> SiteEntries:
	soup = HTMLParser.getSoup("https://www.pi.uni-hannover.de/de/dbs/abschlussarbeiten/")
	main = soup.find("main")
	spans = main.find_all("span")
	texts = [sp.getText() for sp in spans]

	entries = SiteEntries()
	for t in texts:
		title, _, typ = t.replace(u'\xa0', u' ').rpartition(' ')
		entries.add(title, typ.replace('[','').replace(']',''))
	return entries
