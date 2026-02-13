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
life_test = list()
for composer in text_list:
    if re.search(r' \(\d{4}–\d{4}\)$', composer):
        # composers.update(composer.)
        # life = re.search(r'\((\d{4})–(\d{4})\)$', composer)
        life = re.search(r'\((\d{4}–\d{4})\)$', composer.strip("'"))
        life = life.group(1)
        name = re.search(r'^([A-Za-z ]+)', composer.strip("'"))
        name = name.group(1)
        # life_test.append(life.group(1))
        composers.update({name:life})

print(composers)
#separate names and period of life
