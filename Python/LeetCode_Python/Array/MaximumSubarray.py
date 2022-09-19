#!/usr/bin/env python
# coding=utf-8
class Solution: # 201 / 209 test cases passed Time Limit Exceeded
    def maxSubArray(self, nums: List[int]) -> int:
        result = []
        # current = nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            subres = current = nums[i]
            subsum = [subres]
            for j in range(i + 1, len(nums)):
                subres += nums[j]
                subsum.append(subres)
            result.append(max(subsum))
        return max(result)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = current = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            result = max(current, result)
        return result


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxes = nums[0]
        current = nums[0]
        for i in nums[1:]:
            maxes = max(maxes, current + i, i)
            if current + i < i:
                current = i
            else:
                current += i
        return maxes


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i, num in enumerate(nums):
            if i > 0 and dp[i - 1] > 0:
                dp[i] = dp[i - 1] + num
            else:
                dp[i] = num

        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) #状态转移公式
            result = max(result, dp[i]) #result 保存dp[i]的最大值
        return result
