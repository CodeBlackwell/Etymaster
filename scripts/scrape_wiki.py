import bs4 as bs
import urllib2


sauce = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_Latin_words_with_English_derivatives').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

tables = soup.find_all("table", {"class": "wikitable"})

listOfTables = []



for table in tables:
    headers = []
    data = []
    for row in table:
        index = 1
        # check each row to see if it is a header row
        # if hasattr(row, "th") == True:
        #     print({row: row, name: row.name, HoD: 'header'})
        #     headers.append(row.string)
        # if hasattr(row, "td") == True:
        #     print({row: row, name: row.name, HoD:'data'})
        #     data.append(row.string)

    listOfTables.append({ "data": data, "headers": headers })



# {"citation_form": '', "declining_stem": '', "meaning": '', "english_derivatives": ''}
print(listOfTables[0])


print(type(tables))
print(type(tables[0]))
print(type(tables[0].tr))
print(tables[0].tr.get("table"))