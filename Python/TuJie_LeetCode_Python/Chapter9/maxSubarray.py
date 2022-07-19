#!/usr/bin/env python
# coding=utf-8


class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        subCount = 0
        maxCount = nums[0]
        for i in range(len(nums)):
            subCount += nums[i]
            if subCount > maxCount:
                maxCount = subCount
            if subCount < 0:
                subCount = 0
        return maxCount
