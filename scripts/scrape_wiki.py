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

# print(tables)

def validate_anchors(element):
    result = []
    if element.string == None:
        anchors = bs.BeautifulSoup(str(element), 'lxml').find_all("a")
        for anchor in anchors:
            result.append(anchor.string)

        return ", ".join(result)
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
    rowData = {"citation_form": None, "declining_stem": None, "meaning": None, "english_derivatives": None}
    # check each row to see if it is a tag object
    # print(len(bs.BeautifulSoup(row, 'lxml')))
    for td in row:
        # check each <td> tag to ignore all headers and only pass tags
        # assign appropriate keys to all values
        if num_of_elements(row) == 4:

        # @formatter:off
            if type(td) == tag and td.name != 'th':

                if data_row_index == 0:
                    rowData["citation_form"]       = validate_anchors(td)
                    data_row_index = data_row_index + 1

                elif data_row_index == 1:
                    rowData["declining_stem"]      = validate_anchors(td)
                    data_row_index = data_row_index + 1

                elif data_row_index == 2 :
                    rowData["meaning"]             = validate_anchors(td)
                    data_row_index = data_row_index + 1

                elif data_row_index == 3:
                    rowData["english_derivatives"] = validate_anchors(td)
                    break

        # elif num_of_elements(row) == 2:

            # if type(td) == tag and td.name != 'th':
            #     if data_row_index == 0:
            #         rowData["citation_form"]       = td.string
            #         data_row_index = data_row_index + 1
            #
            #     elif data_row_index == 1:
            #         rowData["declining_stem"]      = td.string
            #         data_row_index = data_row_index + 1
            #
            #     elif data_row_index == 2:
            #         rowData["meaning"]             = get_prev_prop(nouns_and_adj, nouns_and_adj_index, "meaning")
            #         data_row_index = data_row_index + 1
            #
            #     elif data_row_index == 3:
            #         rowData["english_derivatives"] = get_prev_prop(nouns_and_adj, nouns_and_adj_index, "english_derivatives")
            #         break
                    # @formatter:on
        # else:
        #     print "empty row"

    if is_empty(rowData) == False:
        nouns_and_adj.append(rowData)
        nouns_and_adj_index = nouns_and_adj_index + 1

print(nouns_and_adj)

verbs_table = []

for row in tables[1]:
    data_row_index = 0
    rowData = {"citation_form": None, "declining_stem": None, "meaning": None, "english_derivatives": None}
    # check each row to see if it is a tag object
    for td in row:
        # assign appropriate keys to all values
        # @formatter:off
        if type(td) == tag and td.name != 'th':
            if data_row_index == 0:
                rowData["citation_form"]       = td.text
                data_row_index = data_row_index + 1

            elif data_row_index == 1:
                rowData["declining_stem"]      = td.text
                data_row_index = data_row_index + 1

            elif data_row_index == 2:
                rowData["meaning"]             = td.text
                data_row_index = data_row_index + 1

            elif data_row_index == 3:
                rowData["english_derivatives"] = td.text
                data_row_index = data_row_index + 1
    #@formatter:on
    if is_empty(rowData) == False:
        verbs_table.append(rowData)
# print(verbs_table)
