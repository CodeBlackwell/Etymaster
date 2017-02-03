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
        # check each row to see if it is a header row
        if hasattr(row, "th"):
            headers.append([row.text])
        elif hasattr(row, "td"):
            data.append(row)
    listOfTables.append({"headers": headers, "data": data})

print(listOfTables[0]['headers'][0])
