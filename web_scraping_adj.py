import re
from bs4 import BeautifulSoup
import unicodedata as u             # attempted solution to u'\u2013' issue
from dateutil.parser import parse   # attempted solution to u'\u2013' issue
import requests
from time import sleep
import csv
from collections import Counter
import matplotlib.pyplot as plt
base_url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page="


def book_info(td):
    """given a BeautifulSoup <td> Tag representing a book, extract the books
    details and return a dict"""
    # u.enconde('ascii', 'ignore')

    title = td.find("div", "thumbheader").a.text.encode('utf-8', errors='ignore')
    by_author = td.find('div', 'AuthorName').text.encode('utf-8', errors='ignore')
    authors = [x.strip() for x in re.sub("^By ", "", by_author).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href").encode('utf-8', errors='ignore')
    isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0]
    month = td.find("span", "directorydate").text.split()[0].encode('utf-8', errors='ignore')
    year = td.find("span", "directorydate").text.split()[1].encode('utf-8', errors='ignore')

    return {
        "title" : title,
        "authors" : authors,
        "isbn" : isbn,
        "month" : month,
        "year" : year
    }

def is_video(td):
    """its a video if it has exactly one pricelabel, and if the stripped text
    inside that pricelabel starts with 'Video'"""
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels)==1 and
            pricelabels[0].text.strip().startswith("Video"))

books = []

NUM_PAGES = 44

for page_num in range(1, NUM_PAGES +1):
    print "souping page", page_num, ",", len(books), "found so far"
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, "html5lib")

    for td in soup('td', 'thumbtext'):
        if not is_video(td):
            books.append(book_info(td))

    # to follow the robot.txt requirements
    sleep(30)

with open('oreilly_data_books.txt', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for i in range(len(books)):
        writer.writerow([books[i]["title"], books[i]["month"], books[i]["year"],
                         books[i]["isbn"], books[i]["authors"]])

#for i in range(len(books)):
#    print "%r \t %r \t %r" % (books[i]["title"], books[i]["month"], books[i]["year"])

#def get_year(book):
#    """book["date"] looks like 'November 2014' so we need to split on the space,
#    then take the second piece"""
#    return int(book["date"].split()[1])

#year_counts = Counter(get_year(book) for book in books if get_year(book) <= 2016)

def int_year(book):
    """book["date"] looks like 'November 2014' so we need to split on the space,
    then take the second piece"""
    return int(book["year"])

year_counts = Counter(int_year(book) for book in books if int_year(book) <= 2016)

print year_counts

years = sorted(year_counts)
book_counts = [year_counts[year] for year in years]
plt.plot(years, book_counts)
plt.axis([1990, 2017, -5, 225])
plt.ylabel("# of data books")
plt.title("Data is Big!")
plt.show()
