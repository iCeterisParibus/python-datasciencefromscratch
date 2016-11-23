import csv

print """
More frequently we'll work with files which have lots of data on each line.
These files are most often separated by commas or tabs, each line has several
fields separated by a comma (or tab).

This can get complicated when you invevitably have files separated with commas,
tabs, and new lines. Thus it's generally better to use Python's 'csv' module (or
the 'pandas' library). For technical reasons you should always work with 'csv'
files in binary mode by including 'b' after the 'r' or 'w'.

See Stack Overflow (http://bit.ly/1L2Y7wl)

If your file has no headers (which means you probably want each row as a 'list',
and which places the burden on you to know what's in each column), you can use
'csv.reader' to iterate over the rows, each of which will be an appropriately
split list.

For example, if we had a tab-delimited file of stock prices:

    6/20/2014    AAPL    90.91
    6/20/2014    MSFT    41.68
    6/20/2014    FB    64.5
    6/19/2014    AAPL    90.86
    6/19/2014    MSFT    41.51
    6/19/2014    FB    63.34

we could process them with:

    with open('tab_delimited_stock_prices.txt', 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            date = row[0]
            symbol = row[1]
            closing_price = float(row[2])
            process(date, symbol, closing_price) # implies doing something to data

*** Currently have not been able to get this code to appropriately read the data
"""

#with open('tab_delimited_stock_prices.txt', 'rb') as f:
#    reader = csv.reader(f, delimiter='\t')
#    for row in reader:
#        date = row[0]
#        symbol = row[1]
#        closing_price = float(row[2])
        # process(date, symbol, closing_price)

print """
If you file has headers:

    date:symbol:closing_price
    6/20/2014:AAPL:90.91
    6/20/2014:MSFT:41.68
    6/20/2014:FB:64.5

you can either skip the header row (with an initial call to 'reader.next()') or
get each row as a 'dict' (with the headers as keys) by using 'csv.DictReader':

    with open('colon_delimited_stock_prices.txt', 'rb') as f:
        reader = csv.DictReader(f, delimiter=':')
        for row in reader:
            date = row["date"]
            symbol = row["symbol"]
            closing_price = float(row["closing_price"])
            process(date, symbol, closing_price) # implies doing something to data
"""

with open('colon_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        # process(date, symbol, closing_price)

# print date
# print symbol
# print closing_price

print """
Even if your file doesn't have headers you can still use '.DictReader' by
passing it the keys as a 'fieldnames' parameter. You can similarly write out
delimited data using 'csv.writer':

    today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB':64.5}

    with open('comma_delimited_stock_prices', 'wb') as f:
        writer = csv.writer(f, delimiter=',')
        for stock, price in today_prices.items():
            writer.writerow([stock, price])

'csv.writer' will do the right thing if your fields themselves have commas in
them. Your own hand-rolled writer probably won't. For example, if you attempt:

    results = [["test1", "success", "Monday"],
               ["test2", "success, kind of", "Tuesday"],
               ["test3", "failure, kind of", "Wednesday"],
               ["test4", "failure, utter", "Thursday"]]
    # don't do this
    with open('bad_csv.txt', 'wb') as f:
        for row in results:
            f.write(",".join(map(str, row))) # might have too many commas
            f.write("\n") # row might have new lines as well

You'll end up with a 'csv' file that looks like:

    test1,success,Monday
    test2,success, kind of,Tuesday
    test3,failure, kind of,Wednesday
    test4,failure, utter,Thursday

and that no one will ever be able to make sense of.
"""
today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB':64.5}

with open('comma_delimited_stock_prices', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])

print """
As an experiement to build more code, I went ahead read our correctly written
'csv' file to show a basic idea of what 'process(data)' implies we're doing.
"""

with open('comma_delimited_stock_prices', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print row[0]+"\t"+row[1]

print '-' * 100

print """
In addition, I went ahead did the same thing with a slightly larger data set,
iris.txt, to show how we can print a small data set to the console. There may
be more efficient ways to do this, but the main thing to be careful of is that
the data set is not so large that you can't make sense of it by looking at a
print out.

    with open('iris.txt', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        print \"var1\"+\"\\t\"+\"var2\"+\"\\t\"+\"var3\"+\"\\t\"+\"var4\"+\"\\t\"+\"var5\"
        for row in reader:
            print (row[0]+\"\\t\"+row[1]+\"\\t\"+row[2]+\"\\t\"+row[3]+\"\\t\"+row[4])

"""

with open('iris.txt', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    print "var1"+"\t"+"var2"+"\t"+"var3"+"\t"+"var4"+"\t"+"var5"
    for row in reader:
        print (row[0]+"\t"+row[1]+"\t"+row[2]+"\t"+row[3]+"\t"+row[4])

print"\n" + ('-' * 100)
