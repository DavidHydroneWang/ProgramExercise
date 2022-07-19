#!/usr/bin/env python
# coding=utf-8


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        maxCash = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            maxCash.append(max(nums[i] + maxCash[i - 2], maxCash[i - 1]))
        return maxCash[-1]
