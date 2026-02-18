from bs4 import BeautifulSoup
import wikipedia
import re
import pandas as pd
import random
import datetime

wiki = wikipedia.WikipediaPage('List of Classical-era composers')
wiki_html = wiki.html()

text = BeautifulSoup(wiki_html, 'html.parser')
# print(text.prettify())
text = text.get_text()

text_list = text.splitlines()

#separate names and period of life
composers = pd.DataFrame(columns=['name', 'birth_year', 'death_year', 'period'])
for composer in text_list:
    if re.search(r' \(\d{4}–\d{4}\)$', composer):
        grouping = re.search(r'([\D]+) \((\d{4})–(\d{4})\)', composer) #need to remove \xa0[de] from name
        name, birth, death= grouping.groups()
        composers.loc[len(composers)] = [name,birth,death,""] #need to convert birth and death into int. right now strs
composers['birth_year'] = pd.to_numeric(composers['birth_year'], downcast='integer', errors='coerce')
composers['death_year'] = pd.to_numeric(composers['death_year'], downcast='integer', errors='coerce')

# def categorize_era(x):
#     if 1600 <= int(x) <= 1760:
#         return "Baroque"
#     elif 1730 <= int(x) <= 1760:
#         return "Classical"
#     elif 1815 <= int(x) <= 1910:
#         return "Romantic"

def categorize_era(x):
    era_tuple = tuple()
    if 1600 <= x <= 1760:
        era_tuple += 'Baroque'
    elif 1730 <= x <= 1820:
        era_tuple += 'Classical'
    elif 1815 <= x <= 1910:
        era_tuple += 'Romantic'

#now categorize composer period given birth and death dates. add era as a column of type list to table
#look through all birth dates. append era to era list (empty list)
#look through all death dates. append era to era list if era does not exist already in list

# era_list = []
# era_list = categorize_era(composers)
composers['period'] = composers.apply(categorize_era, axis=1)
# print(composers)
print(composers)

#prompt user for period. return random composer in period. if lived in overlap, have chance to be in either period

# def return_composer():

