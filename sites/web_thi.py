from entries import SiteEntries
from web import HTMLParser

def website_thi() -> SiteEntries:
	soup = HTMLParser.getSoup("https://www.thi.uni-hannover.de/de/lehre/studien-abschlussarbeiten/")
	m = soup.find("main")
	li = m.find_all("li")
	
	entries = SiteEntries()
	a = [item.find("a") for item in li]
	for i in a:
		entries.add(i.getText(), "All")
	return entries
