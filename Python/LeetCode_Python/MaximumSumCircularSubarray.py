#!/usr/bin/env python
# coding=utf-8
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = 0
        currMaxSum = 0
        currMinSum = 0
        maxSum = -math.inf
        minSum = math.inf

        for a in nums:
            totalSum += a
            currMaxSum = max(currMaxSum + a, a)
            currMinSum = min(currMinSum + a, a)
            maxSum = max(maxSum, currMaxSum)
            minSum = min(minSum, currMinSum)

        return maxSum if maxSum < 0 else max(maxSum, totalSum - minSum)



class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        size = len(nums)

        dp_max, dp_min = nums[0], nums[0]
        max_num, min_num = nums[0], nums[0]
        for i in range(1, size):
            dp_max = max(dp_max + nums[i], nums[i])
            dp_min = min(dp_min + nums[i], nums[i])
            max_num = max(dp_max, max_num)
            min_num = min(dp_min, min_num)
        sum_num = sum(nums)
        if max_num < 0:
            return max_num
        return max(sum_num - min_num, max_num)


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if all(num <= 0 for num in nums):
            return max(nums)

        overall_max, overall_min = float('-inf'), float('inf')
        max_ending_here, min_ending_here = 0, 0

        for num in nums:

            max_ending_here = max(max_ending_here, 0) + num     # if previous max negative, set to zero
            min_ending_here = min(min_ending_here, 0) + num     # if previous min positive, set to zero

            overall_max = max(overall_max, max_ending_here)
            overall_min = min(overall_min, min_ending_here)

        return max(overall_max, sum(nums) - overall_min)
