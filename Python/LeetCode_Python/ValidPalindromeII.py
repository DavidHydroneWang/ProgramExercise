#!/usr/bin/env python
# coding=utf-8
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return check(i, j - 1) or check(i + 1, j)
            i, j = i + 1, j - 1

        return True


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        i = 0

        while i < n // 2:

            if s[i] != s[n - 1 - i]:
                del_front = s[i + 1:n - i]
                del_back = s[i:n - 1 - i]
                return del_front == del_front[::-1] or del_back == del_back[::-1]

            i += 1

        return True
