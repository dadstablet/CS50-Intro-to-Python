import pandas as pd
import requests
from bs4 import BeautifulSoup

wiki_url = 'https://en.wikipedia.org/wiki/List_of_Classical-era_composers'

text = BeautifulSoup(wiki_url, 'html.parser')
print(text)
