from bs4 import BeautifulSoup
import wikipedia
import re

wiki = wikipedia.WikipediaPage('List of Classical-era composers')
wiki_html = wiki.html()

text = BeautifulSoup(wiki_html, 'html.parser')
# print(text.prettify())
text = text.get_text()

text_list = text.splitlines()

composers = {}
for composer in text_list:
    if re.search(r' \(\d{4}–\d{4}\)$', composer):
        # composers.update(composer.)
        life = re.search(r' \(\d{4}–\d{4}\)$', composer)


#separate names and period of life
