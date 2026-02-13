from bs4 import BeautifulSoup
import wikipedia

wiki = wikipedia.WikipediaPage('List of Classical-era composers')
wiki_html = wiki.html()

text = BeautifulSoup(wiki_html, 'html.parser')
# print(text.prettify())
print(text.get_text())

#next steps: return eras, create list of composers based on eras
#composers aren't in wikitable, rather a bulletted list under designated era

# eras = text.find_all('h2') #maybe add id=input of user
# eras = text.find_all(class_='mw-heading mw-heading2')
# print(eras)
