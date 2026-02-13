import wikipedia

wiki = wikipedia.WikipediaPage('List of Classical-era composers')

html = wiki.html

print(html)
