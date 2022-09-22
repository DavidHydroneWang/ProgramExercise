#!/usr/bin/env python
# coding=utf-8
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []

        for num in nums:
            list_nb =  self.binary_search(num, LIS)
            print(LIS)
            if list_nb == len(LIS) - 1:
                LIS.append(num)
            else:
                LIS[list_nb + 1] = min(num, LIS[list_nb + 1])

        return len(LIS)

    def binary_search(self, num, LIS):
        left, right = 0, len(LIS) - 1
        while left <= right:
            mid = (left + right) // 2
            if num <= LIS[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return right


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = [1 for _ in nums]
        for i in range(len(nums)):
            currentNum = nums[i]
            for j in range(i):
                otherNum  = nums[j]
                if otherNum < currentNum and length[j] + 1 >= length[i]:
                    length[i] = length[j] + 1
        return max(length)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        result = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i]) #取长的子序列
        return result
