#!/usr/bin/env python
# coding=utf-8


class Solution:
    def missingNumber(self, nums):
        try:
            n = (set(range(len(nums) + 1)) - set(nums)).pop()
        except KeyError as e:
            return
        else:
            return n
