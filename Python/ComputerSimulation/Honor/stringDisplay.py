#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    linestr = line.replace('\n', '').split(' ')
    res = []

    for s in linestr:
        s = sorted(set(s))
        s = ''.join(s)
        index = 0
        while index < len(s) - 8:
            res.append(s[index: index + 8])
            index += 8
        if len(s) != index:
            res.append(s[index:] + (8 - len(s) + index) * '0')

    res2 = res[:]
    for s in res:
        temp = res[:]
        temp.remove(s)
        tempstr = ''.join(temp)
        if len(s.strip('0')) < 8 and s.strip('0') in tempstr:
            res.remove(s)

    res2 = ' '.join(res)
    print(res2)
