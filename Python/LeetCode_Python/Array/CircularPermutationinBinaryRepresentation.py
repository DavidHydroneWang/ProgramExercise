#!/usr/bin/env python
# coding=utf-8
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ i ^ i >> 1 for i in range(1 << n)]


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def helper(i):
            if i == 1:
                return [0, 1]
            temp = helper(i - 1)
            power = 2 ** (i - 1)
            return temp + [power + t for t in temp[::-1]]

        perms = helper(n)
        #print(perms)
        i = perms.index(start)
        return perms[i:] + perms[:i]
