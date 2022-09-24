#!/usr/bin/env python
# coding=utf-8
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        robber = [nums[0], nums[1], nums[2] + nums[0]]

        for i in range(3, len(nums)):
            robber.append(max(nums[i] + robber[i - 2], nums[i] + robber[i - 3]))

        return max(robber)
