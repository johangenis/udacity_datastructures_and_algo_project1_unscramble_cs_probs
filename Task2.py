"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone
during September 2016.".

Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import deque, defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

calls_dict = defaultdict(int)
output = "{} spent the longest time, <total time> {} \
seconds, on the phone during September 2016."

for caller, callee, timestamp, duration in calls:
    calls_dict[caller] += int(duration)
    calls_dict[callee] += int(duration)

longest_duration = max(calls_dict.items(), key = lambda x: x[1])

print(output.format(*longest_duration))
