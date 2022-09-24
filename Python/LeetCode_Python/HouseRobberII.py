#!/usr/bin/env python
# coding=utf-8
class Solution: #  55 / 75 test cases passed. Status: Wrong Answer
    def rob(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = nums[i]
            elif i == 1:
                res[i] = max(nums[0], nums[1])
            elif i == 2:
                if i == len(nums) - 1:
                    res[i] = max(nums[i], nums[i - 1])
                else:
                    res[i] = max(nums[i] , nums[i - 1], nums[0])
            elif i == 3:
                res[i] = max(sum([nums[j] for j in range(0, i + 1, 2) ]), sum([nums[j] for j in range(1, i + 1, 2) ]), nums[i - 2] + nums[i])
            else:
                if i % 2 == 0:

                    res[i] = max(sum([nums[j] for j in range(2, i + 2, 2) ]), res[i - 1], res[i - 2] + nums[i])
                else:
                    res[i] = max(sum([nums[j] for j in range(0, i + 1, 2) ]), sum([nums[j] for j in range(1, i + 2, 2) ]), nums[i - 2] + nums[i])
        #print(res)
        return max(res)


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            size = len(nums)
            if size == 1:
                return nums[0]
            dp = [0 for _ in range(size)]
            for i in range(size):
                if i == 0:
                    dp[i] = nums[0]
                elif i == 1:
                    dp[i] = max(nums[i - 1], nums[i])
                else:
                    dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        else:
            return max(helper(nums[1:]), helper(nums[:-1]))
