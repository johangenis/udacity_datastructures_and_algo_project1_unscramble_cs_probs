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
    dist_num_cnt = 0
    for i in a_list:
        if i[0] not in dist_nums:
            dist_nums.add(i[0])
            dist_num_cnt += 1
    return dist_num_cnt

print(output.format(distinct_nums(texts, calls)))
