from entries import SiteEntries
from web import HTMLParser

def website_se() -> SiteEntries:
	soup = HTMLParser.getSoup("https://www.pi.uni-hannover.de/de/se/studentische-arbeiten/angebote/")
	tables = soup.find("table", {"class": "contenttable"})
	table_body = tables.find('tbody')
	rows = table_body.find_all('tr')
	
	entries = SiteEntries()
	for row in rows:
		t = [t for t in row.find_all(text=True) if t != ' ']
		entries.add(t[0], t[2], list(t[1]))
	return entries
