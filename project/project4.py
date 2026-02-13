from bs4 import BeautifulSoup
import wikipedia
import re
import pandas as pd
import datetime

wiki = wikipedia.WikipediaPage('List of Classical-era composers')
wiki_html = wiki.html()

text = BeautifulSoup(wiki_html, 'html.parser')
# print(text.prettify())
text = text.get_text()

text_list = text.splitlines()

#separate names and period of life
composers = {}
life_test = list()
df = pd.DataFrame(columns=["name", "birth_year", "death_year", "period"])
for composer in text_list:
    if re.search(r' \(\d{4}–\d{4}\)$', composer):
        # composers.update(composer.)
        # life = re.search(r'\((\d{4})–(\d{4})\)$', composer)
        # name.strip('\xa0[de]')
        # life = re.search(r'\((\d{4}–\d{4})\)', composer)
        # life = life.group(1)
        # name = re.search(r'([\D]+ )', composer)
        # name = name.group(1).strip()
        # life_test.append(life.group(1))
        grouping = re.search(r'([\D]+) \((\d{4})–(\d{4})\)', composer) #need to remove \xa0[de] from name
        name, birth, death= grouping.groups()
        df.loc[len(df)] = [name,birth,death,""]
print(df)

def categorize_era(x):
    if 1400 <= x <= 1600:
        return "Renaissance"
    elif 1600 <= x <= 1760:
        return "Baroque"
    elif 1730 <= x <= 1760:
        return "Classical"
    elif 1815 <= x <= 1910:
        return "Romantic"
    elif 1890 <= x <= 1950:
        return "Modernist"
    elif 1930 <= x <= datetime.date.today():
        return "Postmodernist"

#if life in era. return composer
# eras = {
#     Medieval : '500-1400',
#     Renaissance : '1400-1600',
#     Baroque : '1600-1760',
#     Classical : '1730-1820',
#     Romantic : '1815-1910',
#     Modernist : '1890-1950',
#     Postmodernist : '1930-2026'
# }

