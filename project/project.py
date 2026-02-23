""" Classical Composer Suggestor """

from bs4 import BeautifulSoup
import wikipedia
import re
import pandas as pd


def get_composer_table():
    """create table of composer name, birth, death, and period based on wikipedia page"""
    wiki = wikipedia.WikipediaPage('List of Classical-era composers')
    wiki_html = wiki.html()
    text = BeautifulSoup(wiki_html, 'html.parser') #using BS to read the html provided by wikipedia method
    text_list = text.get_text().splitlines() #since in bulletted list on wikipage, use /n to know where composer data end/begin

    composers = pd.DataFrame(columns=['name', 'birth_year', 'death_year', 'period'])

    for composer in text_list:
        if re.search(r' \(\d{4}–\d{4}\)$', composer): #lines that end in (YYYY-YYYY) are composers
            grouping = re.search(r'([\D]+) \((\d{4})–(\d{4})\)', composer) #capture name, birth_year, and death_year. unable to figure out how to remove \xa0[de] from name
            name, birth, death= grouping.groups()
            composers.loc[len(composers)] = [name,birth,death,""] #need to convert birth and death into column of ints. right now strs
    composers['birth_year'] = pd.to_numeric(composers['birth_year'], downcast='integer', errors='coerce')
    composers['death_year'] = pd.to_numeric(composers['death_year'], downcast='integer', errors='coerce')
    composers['period'] = [[] for _ in range(len(composers))]

    # now categorize composer period(s) given birth and death dates. fill in empty list column of period
    for index, row in composers.iterrows():
        row['period'].append(categorize_era(row['birth_year']))
        if categorize_era(row['death_year']) not in row['period']:
            row['period'].append(categorize_era(row['death_year']))
        else:
            pass

    return composers

def categorize_era(x):
    """classify the period(s) of composer"""
    if 1600 <= int(x) <= 1760:
        return 'Baroque'
    elif 1730 <= int(x) <= 1820:
        return 'Classical'
    elif 1815 <= int(x) <= 1910:
        return 'Romantic'
    else:
        pass

def select_period(x):
    """possible selection of user inputs that return specified period"""
    x = x.lower().capitalize()
    if x in ['Baroque', 'Bach', 'Vivaldi']:
        return 'Baroque'
    elif x in ['Classical', 'Mozart', 'Beethoven']:
        return 'Classical'
    elif x in ['Romantic', 'Liszt', 'Chopin', 'Rachmaninoff', 'Tchaikovsky', 'Brahms']:
        return 'Romantic'
    else:
        raise ValueError

def main():
    """prompt user for period. return random composers in period"""
    composers = get_composer_table()
    while True: #use a loop that breaks once correct input is provided
        try:
            user_input = select_period(input('Baroque, Classical, or Romantic? '))
            selected_composers = composers[composers['period'].apply(lambda x: user_input in x)]
            rand_comps = selected_composers['name'].sample(3).values
            print(f'Try out {rand_comps[0]}, {rand_comps[1]}, or {rand_comps[2]}')
            break
        except ValueError:
            pass

if __name__ == '__main__':
    main()

# print(get_composer_table())
