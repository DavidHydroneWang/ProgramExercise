#!/usr/bin/env python
# coding=utf-8
import sys
import re

pattern = re.compile(r'^\((\d+), (\d+)\)\s+([+-/*])\s+\((\d+), (\d+)\)$')

for line in sys.stdin:
    linestr = line.strip('\n')
    res = pattern.match(linestr)
    if res is None:
        print('NaN')
    else:
        if res.group(3) == '+':
            out = (int(res.group(1)) + int(res.group(4)), int(res.group(2)) + int(res.group(5)))
            print(out)
        elif res.group(3) == '-':
            out = (int(res.group(1)) - int(res.group(4)), int(res.group(2)) - int(res.group(5)))
            print(out)
#    print(res.group(5))
