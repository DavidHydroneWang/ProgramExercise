#!/usr/bin/env python
# coding=utf-8


class Solution:
    def find_rotate(self, nums):
        target = nums[0]

        lo = 1
        for i in range(1, len(nums)):
            if nums[i] == target:
                lo += 1
            else:
                break

        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                lo = mid + 1
            else:
                hi = mid

        return mid

    def find_Min(self, nums):
        rotate = self.find_rotate(nums)

        if rotate == len(nums):
            return nums[0]
        return nums[rotate]


class Solution:
    def find_Min(self, nums):
        left, right = 0, len(nums) - 1
        while left < right and nums[left] >= nums[right]:
            mid = (left + right) // 2
            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
