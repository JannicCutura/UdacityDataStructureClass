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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def getNumbers(texts,calls ):
    list_of_phone_numbers=[]
    for record in calls:
        if not record[0] in list_of_phone_numbers:
            list_of_phone_numbers.append(record[0])
        if not record[1] in list_of_phone_numbers:
            list_of_phone_numbers.append(record[1])

    for record in texts:
        if not record[0] in list_of_phone_numbers:
            list_of_phone_numbers.append(record[0])
        if not record[1] in list_of_phone_numbers:
            list_of_phone_numbers.append(record[1])
    return len(list_of_phone_numbers)
print("There are {} different telephone numbers in the records".format(getNumbers(texts,calls )))



