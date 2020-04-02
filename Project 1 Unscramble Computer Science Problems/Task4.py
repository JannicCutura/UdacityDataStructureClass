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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

## first I define four helper fucntions to get lists of callers, called, texters and texted numbers
def getsCalls(calls ):
    get_called=[]
    for record in calls:
        if not record[1] in get_called:
            get_called.append(record[1])
    return get_called

def whoCalls(calls):
    do_calls = []
    for record in calls:
        if not record[0] in do_calls:
            do_calls.append(record[0])
    return do_calls

def getsTexts(texts):
    get_texted = []
    for record in texts:
        if not record[1] in get_texted:
            get_texted.append(record[1])
    return get_texted

def whoTexts(texts):
    text_others = []
    for record in texts:
        if not record[0] in text_others:
            text_others.append(record[0])
    return text_others

# now put it together
def findTelemarketers(texts, calls):
    text_others = whoTexts(texts)
    gets_texted = getsTexts(texts)
    gets_called = getsCalls(calls)
    calls_others = whoCalls(calls)

    telemaketers = list(set(calls_others) - (set(text_others).union(set(gets_texted).union(set(gets_called)))))
    telemaketers.sort()
    return list(telemaketers)




print("These numbers could be telemarketers: ")
for number in findTelemarketers(texts, calls):
    print(number)

