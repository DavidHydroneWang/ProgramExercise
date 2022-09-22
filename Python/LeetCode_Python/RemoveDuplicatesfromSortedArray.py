#!/usr/bin/env python
# coding=utf-8
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            else:
                j += 1

        return i + 1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for num in nums:
            if i < 1 or num > nums[i - 1]:
                nums[i] = num
                i += 1

        return i
