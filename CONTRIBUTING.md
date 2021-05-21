# CONTRIBUTING

Currently we support the following sites:
- [SE Uni Hannover](https://www.pi.uni-hannover.de/de/se/studentische-arbeiten/laufende-arbeiten/)
- [DBS Uni Hannover](https://www.pi.uni-hannover.de/de/dbs/abschlussarbeiten/)

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

## Adding a new site

What you need to know in advance: BeautifulSoup4, basic knowledge of python modules

These are the basic steps:
1. Fork and clone this repo
2. Create a new ```web_[YOUR_SITE].py``` file inside ```sites/```
3. Introduce your module to ```config.py```
4. Create a pull request

### 1. Fork and clone this repo
First of all the repo needs to be forked in order to add new files. If you don't know how this works you may google it.

### 2. Create a new web_[YOUR_SITE].py file inside sites/
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

After that you can use methods of bs4 to parse the Data. There are multiple ways and every website is different, so that's the challenging part. In the end you should have a string containing the title of the thesis and another one containing the degree of the thesis (Bachelor/Master).
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

### 3. Introduce your module to config.py


### 4. Create a pull request
At the end a pull request is necessary to add the files to the original repo. If you don't know how this works you may google it.
