#!/usr/bin/env python
# coding=utf-8


class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void
        """
        length = len(s)
        if length < 2:
            return
        for i in range(length//2):
            s[i], s[length - i - 1] = s[length - i - 1], s[i]
        return


class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void
        """
        s.reverse()
        return
