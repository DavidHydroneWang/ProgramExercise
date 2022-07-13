#!/usr/bin/env python
# coding=utf-8


class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        if len(s) != len(t):
            return False
        sList = list(s)
        tList = list(t)
        sList.sort()
        tList.sort()
        for i in range(len(s)):
            if sList[i] == tList[i]:
                continue
            else:
                return False
        return True


class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        if len(s) != len(t):
            return False
        sList = list(s)
        for word in t:
            try:
                sList.remove(word)
            except ValueError:
                return False
        return True
