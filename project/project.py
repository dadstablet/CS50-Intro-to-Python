import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(user_agent='MusicProjectBot (nzakaria@hl.agency)', language='en')
page_py = wiki_wiki.page('List of Classical-era composers')

# print(f'Page - Title: {page_py.title}')
# print(page_py.summary[0:60])

# def print_sections(sections, level=0):
#     section_list = list()
#     for s in sections:
#         section_list.append(s)
#     print(section_list)

# print_sections(page_py.sections)

"""
"""
wiki_html = wikipediaapi.Wikipedia(
    user_agent='MyProjectName (merlin@example.com)',
    language='en',
    extract_format=wikipediaapi.ExtractFormat.HTML
)
p_html = wiki_html.page("Test 1")
print(p_html.text)


#Ask user of music era of interest. Return list of composers of that era
def main():
    input('Select Era: ')
