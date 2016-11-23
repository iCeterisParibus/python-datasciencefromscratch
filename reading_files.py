# Reading Files section

import re
from collections import Counter

print '-' * 100
print """
Reading Files

You can explicitly read from and write to files directly in your code.
"""

print '-' * 100
print """
The first step to working iwth a text file is to obtain a file object
using 'open':

    # 'r' means read-only
    file_for_reading = open('reading_file.txt', 'r')

    # 'w' is write -- will distroy the file if it already exists
    file_for_writing = open('writing_file.txt', 'w')

    # 'a' is append -- for adding to the end of the file
    file_for_appending = open('appending_file.txt', 'a')

    # don't forget to close your files when you're done
    file_for_writing.close()
"""

# 'r' means read-only
file_for_reading = open('reading_file.txt', 'r')

# 'w' is write -- will distroy the file if it already exists
file_for_writing = open('writing_file.txt', 'w')

# 'a' is append -- for adding to the end of the file
file_for_appending = open('appending_file.txt', 'a')

# don't forget to close your files when you're done
file_for_writing.close()

print '-' * 100
print """
Because it is easy to forget to close your files, you should always use them in
a 'with' block, at the end of which they will be closed automatically:

    with open(filename, 'r') as f:
         data = function_that_gets_data_from(f)

    At this point f has already been closed, so don't try to use it
    process(data)
"""

# with open(filename, 'r') as f:
#     data = function_that_gets_data_from(f)

# At this point f has already been closed, so don't try to use it
# process(data)

print '-' * 100
print """
If you need to read a whole text file, you can just iterate over the lines of
the file using 'for':

    starts_with_hash = 0

    with open('iris.txt', 'r') as f:
        for line in f:
            if re.match('^#', line):
                starts_with_hash += 1
"""

starts_with_hash = 0

with open('iris.txt', 'r') as f:
    for line in f:
        if re.match('^#', line):
            starts_with_hash += 1

print """
Every line you get this way ends in a newline character, so you'll often want
to 'strip()' it before doing anything with it.

For example, imagine you have a file full of email addresses, one per line, and
that you need to generate a histogram of the domains. The rules for correctly
extracting domains are somewhat subtle (e.g., the Public suffix List
(https://publicsuffix.org)), but a good first approximation is to just take the
parts of the email addresses that come after the '@'. (Which gives the wrong
answer for email addresses like 'joel@mail.datascienster.com')

    def get_domain(email_addresses):
        \"\"\"split on '@' and return the last piece\"\"\"
        return email_address.lower().split(\"@\")[-1]

    with open('email_addresses.txt', 'r') as f:
        domain_counts = Counter(get_domain(line.strip())
                                for line in f
                                if \"@\" in line)
"""

def get_domain(email_address):
    """split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]

with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line)

print """
%s
""" % (domain_counts)
print '-' * 100
