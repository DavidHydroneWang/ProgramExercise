#!/usr/bin/env python
# coding=utf-8


class Solition:
    def singleNumber(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        nums.sort()
        length = len(nums)
        if length < 3:
            return nums[0]
        i = 0
        while i < length - 2:
            if nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i += 2
        return nums[-1]


class Solition:
    def singleNumber(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        nums.sort()
        n = list(set(nums[::2]) - set(nums[1::2]))[0]
        return n
