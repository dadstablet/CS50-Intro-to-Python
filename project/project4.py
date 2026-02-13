from bs4 import BeautifulSoup
import wikipedia

wiki = wikipedia.WikipediaPage('List of Classical-era composers')
wiki_html = wiki.html()

text = BeautifulSoup(wiki_html, 'html.parser')
# print(text.prettify())
text = text.get_text()

list_of_page = []
for /n in text:
    list_of_page.append
