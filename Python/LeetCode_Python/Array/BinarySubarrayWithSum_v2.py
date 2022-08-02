#!/usr/bin/env python
# coding=utf-8
import collections


class Solution:
    def subarraySum(self, Array, Sum):
        result = 0
        accumulated_sum = 0
        lookup = collections.defaultdict(int)
        lookup[0] = 1
        for num in Array:
            accumulated_sum += num
            result += lookup[accumulated_sum - Sum]
            lookup[accumulated_sum] += 1
        return result
