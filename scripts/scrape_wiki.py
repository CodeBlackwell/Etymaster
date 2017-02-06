import bs4 as bs
import urllib2
import json

sauce = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_Latin_words_with_English_derivatives').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

tables = soup.find_all("table")
keepers = []
keepers.append(tables[1])
keepers.append(tables[3])
keepers.append(tables[5])
tables = keepers

nav_string = type(tables[0].tr.next_sibling)
tag = type(tables[0].tr)


def is_empty(hash):
    empty = True
    for key in hash:
        if hash[key] != None:
            empty = False
    return empty

def get_prev_props(row, property):
    if is_empty(row) == True:
        get_prev_props(row)


nouns_and_adjectives = []
nouns_and_adjectives_table_index = 0
for row in tables[0]:
    row_index = 0
    rowData = {"citation_form": None, "declining_stem": None, "meaning": None, "english_derivatives": None}
    # check each row to see if it is a tag object
    for td in row:
        # check each <td> tag to ignore all headers and only pass tags
        # assign appropriate keys to all values
        # @formatter:off
        if type(td) == tag and td.name != 'th' and len(row) == 4:
            if row_index == 0:
                rowData["citation_form"]       = td.string
                row_index = row_index + 1

            elif row_index == 1:
                rowData["declining_stem"]      = td.string
                row_index = row_index + 1

            elif row_index == 2:
                rowData["meaning"]             = td.string
                row_index = row_index + 1

            elif row_index == 3:
                rowData["english_derivatives"] = td.string
                break
    # @formatter:on
        elif type(td) == tag and td.name != 'th' and len(row) == 2:
            if row_index == 0:
               rowData["citation_form"]       = td.string
               row_index = row_index + 1

            elif row_index == 1:
               rowData["declining_stem"]      = td.string
               row_index = row_index + 1

            elif row_index == 2:
               rowData["meaning"]             = table[]
               row_index = row_index + 1

            elif row_index == 3:
               rowData["english_derivatives"] = td.string
               break
       # @formatter:on
    if is_empty(rowData) == False:
        nouns_and_adjectives.append(rowData)
    nouns_and_adjectives_table_index += 1
# print(nouns_and_adjectives)

verbs_table = []

for row in tables[1]:
    row_index = 0
    rowData = {"citation_form": None, "declining_stem": None, "meaning": None, "english_derivatives": None}
    # check each row to see if it is a tag object
    for td in row:
        # assign appropriate keys to all values
        # @formatter:off
        if type(td) == tag and td.name != 'th':
            if row_index == 0:
                rowData["citation_form"]       = td.text
                row_index = row_index + 1

            elif row_index == 1:
                rowData["declining_stem"]      = td.text
                row_index = row_index + 1

            elif row_index == 2:
                rowData["meaning"]             = td.text
                row_index = row_index + 1

            elif row_index == 3:
                rowData["english_derivatives"] = td.text
                row_index = row_index + 1
    #@formatter:on

    if is_empty(rowData) == False:
        verbs_table.append(rowData)
# print(verbs_table)
