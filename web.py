from bs4 import BeautifulSoup
import requests

class HTMLParser:
	@staticmethod
	def getSoup(url) ->	BeautifulSoup:
		header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1'}
		page = requests.get(url, headers=header)
		return BeautifulSoup(page.content, 'html.parser')
