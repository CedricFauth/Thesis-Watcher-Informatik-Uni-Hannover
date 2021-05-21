from sites.sites import sites
from colorama import Fore, Back, Style
import requests


def main():
	for name, fun in sites.items():
		print('{}{} {:<79}{}'.format(Fore.BLACK,Back.WHITE,name,Style.RESET_ALL))
		try:
			entries = fun()
		except requests.exceptions.RequestException as _:
			print('{} {} {}'.format(Fore.RED, 'network error', Style.RESET_ALL))
		else:
			print('{}{}{}'.format(Fore.WHITE, entries, Style.RESET_ALL))

if __name__ == "__main__":
	main()
