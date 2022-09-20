#!/usr/bin/env python
# coding=utf-8
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] < nums[i + 1]:
                return nums[i]


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1      # len(nums) - 1 is always even

        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:                # take lower even index
                mid -= 1

            if mid + 1 == len(nums) or nums[mid + 1] != nums[mid]:
                right = mid
            else:
                left = mid + 2

        return nums[left]


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m

        return nums[l]
