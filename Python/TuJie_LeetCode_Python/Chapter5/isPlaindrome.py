#!/usr/bin/env python
# coding=utf-8


class Solution:
    def isPlaindrome(self, s: 'str') -> 'bool':
        if len(s) < 2:
            return True
        sList = []
        s = s.lower()
        for word in s:
            if word.isalnum():
                sList.append(word)
        n = len(sList) // 2
        if sList[:n] == sList[::-1][:n]:
            return True
        return False


class Solution:
    def isPlaindrome(self, s: 'str') -> 'bool':
        if len(s) < 2:
            return True
        s = s.lower()
        left = 0
        right = len(s) - 1
        while right - left > 0:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right += 1
                continue
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
