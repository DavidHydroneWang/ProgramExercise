#!/usr/bin/env python
# coding=utf-8


class Solution:
    def romanToInt(self, s):
        romanDic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        doubleDic = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        allsum = 0
        i = 0
        while i < len(s):
            try:
                s[i:i + 2]
            except IndexError as e:
                allsum += romanDic[s[i]]
                i += 1
            else:
                if s[i: i + 2] in doubleDic.keys():
                    allsum += doubleDic[s[i: i + 2]]
                    i += 2
                else:
                    allsum += romanDic[s[i]]
                    i += 1
        return allsum
