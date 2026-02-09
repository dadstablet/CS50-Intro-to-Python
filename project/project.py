import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(user_agent='MusicProjectBot (nzakaria@hl.agency)', language='en')
page_py = wiki_wiki.page('Python_(programming_language)')

page_py = wiki_wiki.page('Python_(programming_language)')
print(page_py.exists("List of Classical-era composers"))

#Ask user of music era of interest. Return list of composers of that era
def main():
    input('Select Era: ')
