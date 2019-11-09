# usr/bin/env/ python3
# *-* coding:utf-8 *-*

import pprint

message = 'It was a nice cold day in April, and the clocks were' +\
          'strinking thirteen'
# count: dict[str, int] = {}
count = {}

for i in message:
    count.setdefault(i, 0)
    count[i] += 1

pprint.pprint(count)
