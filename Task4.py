"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in \
lexicographic order with no duplicates.

Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

tele_marketers = []
output = "These numbers could be telemarketers: "

def find_telemarketers(lst):
    for row in lst:
        if row[0] not in tele_marketers:
            tele_marketers.append(row[0])
    return tele_marketers

find_telemarketers(calls)
print(output)
for tel_no in sorted(tele_marketers):
    print(tel_no)
