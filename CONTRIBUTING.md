# CONTRIBUTING

Contributors can add new sites quite simple. The program was designed with modularity in mind.
The following chapters describe how to add new sites.

## Project Structure
```
|- main.py           -- executes the program and controls output
|- web.py            -- module for fetching websites (used by web_[...].py modules)
|- entries.py        -- module for storing topics for one site (used by web_[...].py modules)
|- sites/
   |- config.py      -- used by main.py for executing functions in web_[...].py modules
   |- web_[NAME].py  -- contains actual code for fetching and parsing thesis information from website [NAME]
   |- ...
```

## Fixing Bugs
Feel free to create pull requests for fixed bugs.

## Improving code other than adding a new site
Feel free to create pull requests!

## Adding a new site

What you need to know in advance: BeautifulSoup4, basic knowledge of python modules

These are the basic steps:
1. Fork and clone this repo
2. Create a new ```web_[YOUR_SITE].py``` file inside ```sites/```
3. Introduce your module to ```config.py```
4. Create a pull request

### 1. 
First of all the repo needs to be forked in order to add new files. If you don't know how this works you may google it.

### 2. 
This is the most important step. The file should consist of one or multiple functions and is responsible for parsing the content of your specified website.

The following example should demonstrate how such a file could look like.

First you need to import SiteEntries which can hold the theses data. HTMLParser also needs to be imported and is used for fetching webpage content.

```python
from entries import SiteEntries
from web import HTMLParser
```

The main function signature needs to look like below (name has to be different). It needs to return an instance of SiteEntries that stores all parsed data:
```python
def website_se() -> SiteEntries:
```

You need to create an object of type SiteEntries. This will be used soon to store theses and needs to be returned at the end. HTMLParser.getSoup takes the website URL and returns a BeautifulSoup Object. 
```python
  entries = SiteEntries()
  soup = HTMLParser.getSoup("https://www.pi.uni-hannover.de/de/se/studentische-arbeiten/angebote/")
```

After that you can use methods of bs4 to parse the Data. There are multiple ways and every website is different, so that's the challenging part. In the end you should have a string containing the title of the thesis and another one containing the degree of the thesis (Bachelor/Master or any other degree).
```python
  table_body = tables.find('tbody')
  rows = table_body.find_all('tr')

  entries = SiteEntries()
  # iterating over all rows in a table of thesis topics
  for row in rows:
    # extracting texts from collums
    t = [t for t in row.find_all(text=True) if t != ' ']
    title = t[0] # storing title string
    deg = t[2] # storing degree string
```

Now you can add the title degree pairs into the SiteEntries Object. Each .add call should insert a new topic to the SiteEntries object. 
The method add(title, thtype, others=None) accepts 3 arguments but the latter one is not used currently: The title of the thesis, the degree, and other information as a list. The last argument can be ignored for now.
```python
    entries.add(title, deg)
  return entries
```

After the for loop every topic is now listed inside the SiteEntries object. Now it needs to be returned. This data will be used by other modules to generate the output.

```python
from entries import SiteEntries
from web import HTMLParser

def website_[...]() -> SiteEntries:
  entries = SiteEntries()
  soup = HTMLParser.getSoup("https://www.[...]/studentische-arbeiten/angebote/")

  [...] # parsing data from soup

  for row in rows:
    [...]
    entries.add(title, deg)
  return entries
```

### 3. 
Nearly done! The last step is to introduce your ```web_[...].py``` file to the rest of the program. In order to do that you need to edit the ```config.py```
file in ```sites/```.
It looks like this:
```python
from sites.web_se import *
from sites.web_dbs import *

sites = {
	# "Name des Instituts" : Funktionsname,  [OHNE '()']
	"Software Engineering" : website_se,
	"Datenbanken und Informationssysteme" : website_dbs,
}
```
Import your module using ```from sites.web_[...] import *``` and in the dict add a new line: ```"name of site" : your_main_function```. You need to refer to your 'main' function inside your ```web_[...].py``` file. Don't use `()` here because that would run the function.

### 4. 
At the end a pull request is necessary to add the files to the original repo. If you don't know how this works you may google it.
