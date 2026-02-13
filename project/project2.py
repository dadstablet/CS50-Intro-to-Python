import wikipedia

wiki = wikipedia.WikipediaPage('List of Classical-era composers')

categories = wiki.categories

print(categories)
