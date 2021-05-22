from entries import SiteEntries
from web import HTMLParser

def website_sra() -> SiteEntries:
	soup = HTMLParser.getSoup("https://www.sra.uni-hannover.de/Theses/open.html")
	divTheses = soup.find_all('div', {"class": "object thesis"})
	entries = SiteEntries()
	for obj in divTheses:
		title = obj.find('p', {"class" : "media-heading"}).getText()
		deg = obj.find('i').getText().replace('\n', '').replace(' ', '')[:-6]
		entries.add(title, deg)
	return entries
