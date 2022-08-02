#!/usr/bin/env python
# coding=utf-8
import bisect
import collections


class Solution:
    def countSmaller(self, nums):
        x = []
        result = []

        for i in nums[::-1]:
            result.append(bisect.bisect_left(x, i))
            bisect.insort(x, i)

        return result[::-1]


class Solution:
    def countSmaller(self, nums):
        count = collections.Counter(nums)
        for i in range(max(nums) + 1):
            count[i] += count[i - 1]

        return [count[i - 1] for i in nums]


class Solution:
    def countSmaller(self, nums):
        sorted_nums = sorted(nums)
        return [bisect.bisect_left(sorted_nums, i) for i in nums]
