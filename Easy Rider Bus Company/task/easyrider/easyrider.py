# Write your code here
import json
import re

buses = json.loads(input())


errors = set()
missed = set()

for bus in buses:
    if bus['stop_type'] == 'O':
        errors.add(bus['stop_name'])
    else:
        missed.add(bus['stop_name'])
if missed.intersection(errors):
    print('Wrong stop type:',sorted([x for x in missed.intersection(errors)]))
else:
    print('OK')