import bs4 as bs
import urllib2
import regex
sauce = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_Latin_words_with_English_derivatives').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

tables = soup.find_all("table", {"class": "wikitable"})

listOfTables = []

def translateHyphen(string):
    string = regex.sub('\u0101', '-', string)
    return string

nav_string = type(tables[0].tr.next_sibling)
tag = type(tables[0].tr)
# <class 'bs4.element.Tag'>
# <class 'bs4.element.NavigableString'>
# print(type(tables) == )
for table in tables:
    data = []
    for row in table:
        index = 0
        rowData = {"citation_form": None, "declining_stem": None, "meaning": None, "english_derivatives": None}
        # check each row to see if it is a tag object
        for td in row:
            # check each <td> tag to ignore all headers and only pass tags
            if type(td) == tag and td.name != 'th':
                if index == 0:
                    rowData["citation_form"] = td.text
                    index = index + 1
                    translateHyphen(rowData["citation_form"])

                elif index == 1:
                    rowData["declining_stem"] = td.text
                    index = index + 1
                    translateHyphen(rowData["declining_stem"])

                elif index == 2:
                    rowData["meaning"] = td.text
                    translateHyphen(rowData["meaning"])
                    index = index + 1

                elif index == 3:
                    rowData["english_derivatives"] = td.text
                    translateHyphen(rowData["english_derivatives"])
                    break
        data.append(rowData)
print(data)
        # based on current index


        # {"citation_form": '', "declining_stem": '', "meaning": '', "english_derivatives": ''}
        # print(listOfTables[0])

        #
        # print(type(tables))
        # print(type(tables[0]))
        # print(type(tables[0].tr.next_sibling)) #<class 'bs4.element.NavigableString'>
        #
        # print(type(tables[0].tr)) # <class 'bs4.element.Tag'> .text , next/prev_sibling,

        # print(tables[0].tr.get("table"))
