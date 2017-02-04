import bs4 as bs
import urllib2


sauce = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_Latin_words_with_English_derivatives').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

tables = soup.find_all("table", {"class": "wikitable"})

listOfTables = []

nav_string = tables[0].tr.next_sibling
tag = tables[0].tr
# <class 'bs4.element.Tag'>
# <class 'bs4.element.NavigableString'>
# print(type(tables) == )
for table in tables:
    headers = []
    data = []
    for row in table:

        # check each row to see if it is a tag object
            for td in row:
                if type(td) == type(tag):
                    

# {"citation_form": '', "declining_stem": '', "meaning": '', "english_derivatives": ''}
# print(listOfTables[0])

#
# print(type(tables))
# print(type(tables[0]))
# print(type(tables[0].tr.next_sibling)) #<class 'bs4.element.NavigableString'>
#
# print(type(tables[0].tr)) # <class 'bs4.element.Tag'> .text , next/prev_sibling,

# print(tables[0].tr.get("table"))