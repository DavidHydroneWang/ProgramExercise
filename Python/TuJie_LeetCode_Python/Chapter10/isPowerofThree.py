#!/usr/bin/env python
# coding=utf-8


class Solution:
    def isPowerofThree(self, n):
        power3 = lambda i : pow(3, i)
        i = 0
        while power3(i) <= n:
            if power3(i) == n:
                return True
            else:
                i += 1
        return False
