"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."

Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

output = "There are {} different telephone numbers in the records."

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def distinct_nums(a_list, b_list):
    a_list.extend(b_list)
    dist_nums = set()
    for i in a_list:
        dist_nums.add(i[0])
        dist_nums.add(i[1])
    return len(dist_nums)

print(output.format(distinct_nums(texts, calls)))
