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

output = "These numbers could be telemarketers: "
callers = set()

def find_telemarketers(calls_lst, texts_lst):
    texters_callees = set()
    
    for caller, callee, _, _ in calls_lst:
        callers.add(caller)
        texters_callees.add(callee)
    for texter_s, texter_r, _ in texts_lst:
        texters_callees.add(texter_s)
        texters_callees.add(texter_r)
    callers.difference(callers, texters_callees)

    return callers

find_telemarketers(calls, texts)
print(output)
for tel_no in sorted(callers):
    print(tel_no)
