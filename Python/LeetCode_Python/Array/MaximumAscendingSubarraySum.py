#!/usr/bin/env python
# coding=utf-8
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]

        return max(dp)


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i = 0
        j = i + 1
        nums.append(0)
        #print(nums)
        length = len(nums)
        result = 0
        while j < length:
            if nums[j-1] < nums[j]:
                j += 1
            else:
                result = max(result, sum(nums[i:j]))
                i = j
                j = i + 1
        return result
