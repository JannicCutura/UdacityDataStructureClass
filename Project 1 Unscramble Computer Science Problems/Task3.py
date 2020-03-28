"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import os
#os.chdir('C:\\Users\\janni\\Dropbox\\university\\13 Semester bis zum Lebensende\\2020_03 Udacity Data Structures Class\\Github\\Project 1 Unscramble Computer Science Problems')


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

called_from_bangalore = []
for call in calls:
    caller = call[0]
    called = call[1]
    if caller[0:5] == "(080)":
        called_from_bangalore.append(called)

codes_called_from_bangalore = []


for called in called_from_bangalore:
    # landlines
    if called[0:2] == "(0":
        if called[4:5] == ")":
            area_code = called[0:5]
        if called[5:6] == ")":
            area_code = called[0:6]
        if called[6:7] == ")":
            area_code = called[0:7]

        codes_called_from_bangalore.append(area_code)
    # mobile
    if called[5:6] == " ":
       area_code = called[0:4]
       codes_called_from_bangalore.append(area_code)
    # telemarketers
    if called[0:3] == "140":
       area_code = 140
       codes_called_from_bangalore.append(area_code)

# get unique values:
results = list(set(codes_called_from_bangalore))
results.sort()
print("The numbers called by people in Bangalore have codes:")
for areacode in results:
    print(areacode)




calls_from_bangalore = []
calls_from_bangalore_to_bangalore =[]
num_calls_from_bangalore = 0
num_calls_from_bangalore_to_bangalore = 0
for call in calls:
    caller = call[0]
    called = call[1]
    if caller[0:5] == "(080)":
        calls_from_bangalore.append(call)
        num_calls_from_bangalore +=1
        if  called[0:5] == "(080)":
            calls_from_bangalore_to_bangalore.append(call)
            num_calls_from_bangalore_to_bangalore += 1



print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.". format(round(num_calls_from_bangalore_to_bangalore/num_calls_from_bangalore*100,2)))



