#!/usr/bin/env python
# coding=utf-8
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        for key, value in Counter(nums).items():
            if value == 1:
                return key


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)

        return ones


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return ((sum(set(nums)) * 3) - sum(nums)) // 2
