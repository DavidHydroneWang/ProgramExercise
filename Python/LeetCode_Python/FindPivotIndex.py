#!/usr/bin/env python
# coding=utf-8
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)

        for i in range(len(nums)):
            if (summ - nums[i]) % 2 == 0 and (summ - nums[i]) / 2 == sum(nums[i + 1:]) :
                return i

        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum * 2 + nums[i] == summ:
                return i
            curr_sum += nums[i]
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + nums[i - 1]
        for i in range(n):
            if dp[i] == dp[n] - dp[i + 1]:
                return i

        return -1
