#!/usr/bin/env python
# coding=utf-8
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if s == t:
            #return False
        from collections import Counter
        count_s = Counter(s)
        count_t = Counter(t)
        return count_s == count_t



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        chars = [0] * 26
        for i in range(n):
            chars[ord(s[i]) - ord('a')] += 1
            chars[ord(t[i]) - ord('a')] -= 1
        for c in chars:
            if c != 0:
                return False
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
