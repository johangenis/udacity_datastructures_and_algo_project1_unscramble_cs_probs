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
The list of codes should be print out one per line in lexicographic order \
with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits

Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
# import re

output_a = "The numbers called by people in Bangalore have codes:\n"
output_b = "<percentage> {} percent of calls from fixed lines in Bangalore \
are calls to other fixed lines in Bangalore."
bang_called_codes = set()
bang_fxd_to_fxd = []
bang_fxd_called_cnt = 0
bang_fxd_to_fxd_cnt = 0
bang_fxd_code = '(080)'

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

for row in calls:
    if row[0][0:5] == bang_fxd_code:
        bang_fxd_called_cnt += 1
        bang_called_codes.add(row[1][0:4].strip("()"))

for row in calls:
    if row[0][0:5] == bang_fxd_code and row[1][0:5] == bang_fxd_code:
        bang_fxd_to_fxd_cnt += 1

print(output_a, '\n'.join(sorted(bang_called_codes)))
print(output_b.format((bang_fxd_to_fxd_cnt/bang_fxd_called_cnt)*100))
