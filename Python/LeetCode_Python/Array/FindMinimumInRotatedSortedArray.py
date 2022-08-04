#!/usr/bin/env python
# coding=utf-8


class Solution:
    def find_rotate(self, nums):
        target = nums[0]
        lo = 1
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def find_Min(self, nums):
        rotate = self.find_rotate(nums)

        if rotate == len(nums):
            return nums[0]
        return nums[rotate]


class Solution:
    def find_Min(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] <= nums[right]:
                break
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
