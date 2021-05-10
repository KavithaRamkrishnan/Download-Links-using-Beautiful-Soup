

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import pandas as pd

hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request("....Web URL......", headers=hdr)

html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)


tfile = open('link.txt', 'a')
tfile.write(str(links))
tfile.close()
