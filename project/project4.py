from bs4 import BeautifulSoup
import wikipedia
import re
import pandas as pd

#create table based on wikipedia page
def get_composer_table():
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
    composers['period'] = [[] for _ in range(len(composers))]

    """
    now categorize composer period(s) given birth and death dates.
    """
    for index, row in composers.iterrows():
        row['period'].append(categorize_era(row['birth_year']))
        if categorize_era(row['death_year']) not in row['period']:
            row['period'].append(categorize_era(row['death_year']))
        else:
            pass

    return composers
    # print(composers)

#create function to 'classify' the period(s) of composer
def categorize_era(x):
    if 1600 <= int(x) <= 1760:
        return "Baroque"
    elif 1730 <= int(x) <= 1820:
        return "Classical"
    elif 1815 <= int(x) <= 1910:
        return "Romantic"


#prompt user for period. return random composer in period. if lived in overlap, have chance to be in either period
def main():
    composers = get_composer_table()
    select_period = input("Baroque, Classical, or Romantic? ")
    selected_composers = composers[composers['period'].apply(lambda x: select_period in x)]
    rand_comps = selected_composers['name'].sample(3).values
    print(f'Try out {rand_comps[0]}, {rand_comps[1]}, or {rand_comps[2]}')


if __name__ == '__main__':
    main()
