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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def findLongestTimeandNumber(calls):
    list_of_phone_numbers=[]
    aggregated = dict()

    # first create a list of all phone numbers
    for record in calls:
        if not record[0] in list_of_phone_numbers:
            list_of_phone_numbers.append(record[0])
        if not record[1] in list_of_phone_numbers:
            list_of_phone_numbers.append(record[1])

    # populate a dictionary with those numbers
    for phone_number in list_of_phone_numbers:
        aggregated.update({phone_number : 0})

    # compute talk time
    for call in calls:
        # outgoing
        phone_number = call[0]
        aggregated.update( {phone_number : aggregated[phone_number] + int(call[3])})

        #incoming
        phone_number   = call[1]
        aggregated.update( {phone_number : aggregated[phone_number] + int(call[3])})

    #sort to get largest one
    aggregated = sorted(aggregated.items(), key=lambda x: x[1])
    # get last value
    return list(reversed(list(aggregated)))[0:1]


print("{} spent the longest time, {} seconds, on the phone during September 2016".format(findLongestTimeandNumber(calls)[0][0], str(findLongestTimeandNumber(calls)[0][1])))
