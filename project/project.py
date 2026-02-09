import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(user_agent='MusicProjectBot (nzakaria@hl.agency)', language='en')
page_py = wiki_wiki.page('List of Classical-era composers')

print(f'Page - Title: {page_py.title}')

#Ask user of music era of interest. Return list of composers of that era
def main():
    input('Select Era: ')
