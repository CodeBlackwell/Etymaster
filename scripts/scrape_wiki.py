import bs4 as bs
import urllib2
import regex

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


nouns_and_adjectives = []

for row in tables[0]:
    index = 0
    rowData = {"citation_form": None, "declining_stem": None, "meaning": None, "english_derivatives": None}
    # check each row to see if it is a tag object
    for td in row:
        # check each <td> tag to ignore all headers and only pass tags
        # assign appropriate keys to all values
        if type(td) == tag and td.name != 'th':
            if index == 0:
                rowData["citation_form"] = td.string
                index = index + 1

            elif index == 1:
                rowData["declining_stem"] = td.string
                index = index + 1

            elif index == 2:
                rowData["meaning"] = td.string
                index = index + 1

            elif index == 3:
                rowData["english_derivatives"] = td.string
                break
    if is_empty(rowData) == False:
        nouns_and_adjectives.append(rowData)

verbs_table = []

for row in tables[1]:
    index = 0
    rowData = {"citation_form": None, "declining_stem": None, "meaning": None, "english_derivatives": None}
    # check each row to see if it is a tag object
    for td in row:
        # assign appropriate keys to all values
        # @formatter:off
        if type(td) == tag and td.name != 'th':
            if index == 0:
                rowData["citation_form"]       = td.string
                index = index + 1

            elif index == 1:
                rowData["present_stem"]        = td.string
                index = index + 1

            elif index == 2:
                rowData["perfect_stem"]        = td.string.decode('unicode_escape').encode('ascii','ignore')
                index = index + 1

            elif index == 3:
                rowData["participal_stem"]     = td.string.decode('unicode_escape').encode('ascii','ignore')
                index = index + 1

            elif index == 4:
                rowData["meaning"]             = td.string.decode('unicode_escape').encode('ascii','ignore')

            elif index == 5:
                rowData["english_derivatives"] = td.string.decode('unicode_escape').encode('ascii','ignore')
    #@formatter:on
    if is_empty(rowData) == False:
        verbs_table.append(rowData)
print(verbs_table)