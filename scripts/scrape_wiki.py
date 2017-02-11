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


def validate(element):
    if element.string == None:
        return element.text
    if element.string == unicode('\n'):
        soup = bs.BeautifulSoup(element, 'lxml')
        for noodle in soup:
            print type(noodle)
    else:
        return element.string


def is_empty(hash):
    empty = True
    for key in hash:
        if hash[key] != None:
            empty = False
    return empty


def get_prev_prop(list, index, property):
    index = index - 1
    return list[index][property]


def num_of_elements(row):
    return len(bs.BeautifulSoup(str(row), 'lxml').find_all("td"))


nouns_and_adj = []
nouns_and_adj_index = 0

for row in tables[0]:
    data_row_index = 0
    rowData = {
        "citation_form": None,
        "declining_stem": None,
        "meaning": None,
        "english_derivatives": None}
    for td in row:
        if num_of_elements(row) == 4:
            # @formatter:off
            if type(td) == tag and td.name != 'th':
                valid = validate(td)

                if data_row_index == 0:
                    rowData["citation_form"]       = valid
                    data_row_index = data_row_index + 1

                elif data_row_index == 1:
                    rowData["declining_stem"]      = valid
                    data_row_index = data_row_index + 1

                elif data_row_index == 2 :
                    rowData["meaning"]             = valid
                    data_row_index = data_row_index + 1

                elif data_row_index == 3:
                    rowData["english_derivatives"] = valid
                    break

        if num_of_elements(row) == 2:

            if type(td) == tag and td.name != 'th':
                valid = validate(td)
                prev = nouns_and_adj_index - 1

                if data_row_index == 0:
                    rowData["citation_form"] = valid
                    data_row_index           = data_row_index + 1

                elif data_row_index == 1:
                    rowData["declining_stem"] = valid
                    data_row_index            = data_row_index + 1

            if data_row_index == 2:
                rowData["meaning"] = nouns_and_adj[prev]["meaning"]
                data_row_index     = data_row_index + 1

            elif data_row_index == 3:
                rowData["english_derivatives"] = nouns_and_adj[prev]["english_derivatives"]
                break
                    # @formatter:on

    if is_empty(rowData) == False:
        nouns_and_adj.append(rowData)
        nouns_and_adj_index = nouns_and_adj_index + 1

verbs = []
verbs_index = 0
for row in tables[1]:
    data_row_index = 0
    rowData = {
        "citation_form": None,
        "present_stem": None,
        "perfect_stem": None,
        "participal_stem": None,
        "meaning": None,
        "english_derivatives": None
    }
    # check each row to see if it is a tag object
    for td in row:
        if num_of_elements(row) == 6:

            if type(td) == tag and td.name != 'th':
                if data_row_index == 0:
                    rowData["citation_form"] = td.text
                    data_row_index = data_row_index + 1

                elif data_row_index == 1:
                    rowData["present_stem"] = td.text
                    data_row_index = data_row_index + 1

                elif data_row_index == 2:
                    rowData["perfect_stem"] = td.text
                    data_row_index = data_row_index + 1

                elif data_row_index == 3:
                    rowData["participal_stem"] = td.text
                    data_row_index = data_row_index + 1

                elif data_row_index == 4:
                    rowData["meaning"] = td.text
                    data_row_index = data_row_index + 1

                elif data_row_index == 5:
                    rowData["english_derivatives"] = td.text
                    break

        elif num_of_elements(row) == 5:
            prev = verbs_index - 1
            valid = validate(td)

            if data_row_index == 0:
                rowData["citation_form"] = valid
                data_row_index = data_row_index + 1

            elif data_row_index == 1:
                rowData["present_stem"] = valid
                data_row_index = data_row_index + 1

            elif data_row_index == 2:
                rowData["perfect_stem"] = valid
                data_row_index = data_row_index + 1

            elif data_row_index == 3:
                rowData["participal_stem"] = valid
                data_row_index = data_row_index + 1

            elif data_row_index == 4:
                rowData["meaning"] = verbs[prev]["meaning"]
                data_row_index = data_row_index + 1


            elif data_row_index == 5:
                rowData["english_derivatives"] = verbs[prev]["english_derivatives"]
                break

        elif num_of_elements(row) == 4:
            prev = verbs_index - 1
            valid = validate(td)

            if data_row_index == 0:
                rowData["citation_form"] = valid
                data_row_index = data_row_index + 1

            elif data_row_index == 1:
                rowData["present_stem"] = valid
                data_row_index = data_row_index + 1

            elif data_row_index == 2:
                rowData["perfect_stem"] = valid
                data_row_index = data_row_index + 1

            elif data_row_index == 3:
                rowData["participal_stem"] = valid
                data_row_index = data_row_index + 1

            elif data_row_index == 4:
                rowData["meaning"] = verbs[prev]["meaning"]
                data_row_index = data_row_index + 1

            elif data_row_index == 5:
                rowData["english_derivatives"] = verbs[prev]["english_derivatives"]
                break
                # @formatter:on
    if is_empty(rowData) == False:
        verbs.append(rowData)
        verbs_index = verbs_index + 1

prepositions = []
prepositions_index = 0
for row in tables[2]:
    data_row_index = 0
    rowData = {
        "word": None,
        "meaning": None,
        "prefixes": None,
    }
    # check each row to see if it is a tag object
    for td in row:
        if num_of_elements(row) == 4:

            if type(td) == tag and td.name != 'th':
                if data_row_index == 0:
                    rowData["word"] = td.text
                    data_row_index = data_row_index + 1

                elif data_row_index == 1:
                    rowData["meaning"] = td.text
                    data_row_index = data_row_index + 1

                elif data_row_index == 2:
                    rowData["prefixes"] = td.text
                    data_row_index = data_row_index + 1
                    break
    if is_empty(rowData) == False:
        prepositions.append(rowData)
        prepositions_index = prepositions_index + 1

latin_tables_data = {
    'nouns_and_adj': nouns_and_adj,
    'verbs': verbs,
    'prepositions': prepositions
}

f = open('latin_tables.json', 'w')
f.write(json.dumps(latin_tables_data, sort_keys=True,
                   indent=4, separators=(',', ': ')))
f.close()
