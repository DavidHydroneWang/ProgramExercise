#!/usr/bin/env python
# coding=utf-8


class Solution:
    def findPeakElement(self, nums):
        length = len(nums)
        for i in range(1, length - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i
        if length <= 2:
            return nums.index(max(nums))
        else:
            if nums[0] > nums[1]:
                return 0
            elif nums[-1] > nums[-2]:
                return length - 1
            else:
                return None


class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
