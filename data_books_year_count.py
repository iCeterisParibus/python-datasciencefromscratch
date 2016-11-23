import csv
from collections import Counter
import matplotlib.pyplot as plt

# create empty list for the 5 variables within the data set
titles = []
months = []
years = []
isbns = []
authors =[]

# open the oreilly_data_books.txt file in read-only and process data
with open('oreilly_data_books.txt', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        titles.append(row[0])
        months.append(row[1])
        years.append(row[2])
        isbns.append(row[3])
        authors.append(row[4])

    print '-' * 50

    # count the number of books published each year
    year_counts = Counter(year for year in years if year)
    # print the year counts for observation
    print "Number of Publications for each Year"
    print '-' * 50
    for year, count in sorted(year_counts.most_common(25), reverse=True):
        print str(count) + "\t" + year

    print '-' * 50

    # Count the individual words in each title, no exclusions for common words
    # or symbols, as we are interested in 10 most common words
    title_words_count = Counter(word.lower()
                                for title in titles
                                for word in title.strip().split()
                                if word)

    # print 10 most common words and their count
    print "Ten Most Common Words in Book Titles"
    print '-' * 50
    for word, count in title_words_count.most_common(10):
        print str(count) + "\t" + word

    print '-' * 50

    # Count the frequency of publication in each month and print
    print "Frequency of Publication in each Month"
    print '-' * 50
    month_counts = Counter(month for month in months if month)
    for month, count in month_counts.most_common(12):
        print str(count) + "\t" + month

    print '-' * 50

    # index months in integer form
    months_index = []
    for month in months:
        if month == "January":
            months_index.append(1)
        elif month == "February":
            months_index.append(2)
        elif month == "March":
            months_index.append(3)
        elif month == "April":
            months_index.append(4)
        elif month == "May":
            months_index.append(5)
        elif month == "June":
            months_index.append(6)
        elif month == "July":
            months_index.append(7)
        elif month == "August":
            months_index.append(8)
        elif month == "September":
            months_index.append(9)
        elif month == "October":
            months_index.append(10)
        elif month == "November":
            months_index.append(11)
        elif month == "December":
            months_index.append(12)
        else:
            print "Error"

    month_index_counts = Counter(month for month in months_index if month)

    # count the number of authors and print to the screen the output
    ### authors data written as a string, rather than list. Need to split or read data in correctly
    #author_count = []
    #for author in authors:
    #    author_count.append(len(author))

    #authors_count = Counter(author_count)

    # create new list of years as integers, plot the total number of annual
    # publications over the past 25 years
    years_int = []
    for year in years:
        years_int.append(int(year))

    year_int_counts = Counter(year for year in years_int if year <= 2016)

    years_plt = sorted(year_int_counts)
    book_year_counts = [year_int_counts[year] for year in years_plt]
    plt.plot(years_plt, book_year_counts)
    plt.axis([1990, 2017, -5, 225])
    plt.ylabel("# of data books")
    plt.title("Data is Big!")
    plt.show()

    months_plt = sorted(month_index_counts)
    book_month_counts = [month_index_counts[month] for month in months_plt]
    plt.bar([int(month)-0.4 for month in months_plt], book_month_counts, 0.8)
    plt.xticks(month_index_counts.keys())
    plt.axis([0.4, 12.6, 0, 140])
    plt.ylabel("# of data books")
    plt.title("Publication Frequency each Month")
    plt.show()
