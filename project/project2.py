import wikipedia

wiki = wikipedia.WikipediaPage('List of Classical-era composers')

# Extract the plain text content of the page, excluding images, tables, and other data.
text = wiki.content

# Replace '==' with '' (an empty string)
text = text.replace('==', '')

# Replace '\n' (a new line) with '' & end the string at $1000.
text = text.replace('\n', '')[:-12]
print(text)
