#!/usr/bin/env python
# coding=utf-8


class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        if len(s) == 1:
            return 0
        for i in range(len(s)):
            if s[i] not in s[i + 1:] and s[i] not in s[:1]:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        words = [chr(i) for i in range(97, 123)]
        values = [0] * 26
        wordsDic = dict(zip(words, values))
        for word in s:
            wordsDic[word] += 1
        for i in range(len(s)):
            if wordsDic[s[i]] == 1:
                return i
        return -1
