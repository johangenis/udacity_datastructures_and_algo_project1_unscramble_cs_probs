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

tele_marketers = set()
output = "These numbers could be telemarketers: "

def find_telemarketers(calls_lst, texts_lst):
    calls_lst = [l[:2] for l in calls_lst]
    texts_lst = [l[:2] for l in calls_lst]
    calls_lst.extend(texts_lst)
    for i in calls_lst:
        if i[0] != calls_lst[1] and i[0] != calls_lst[2] and i[0] != calls_lst[3]:
            tele_marketers.add(i[0])
    return tele_marketers

find_telemarketers(calls, texts)
print(output)
for tel_no in sorted(tele_marketers):
    print(tel_no)
