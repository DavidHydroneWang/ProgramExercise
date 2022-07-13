#!/usr/bin/env python
# coding=utf-8


class Solution:
    def containsDuplicate(self, nums):
        """
        type nums: List[int]
        rtype: bool
        """
        for i in range(len(nums) - 1):
            if nums[i] in nums[i + 1:]:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums):
        """
        type nums: List[int]
        rtype: bool
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums):
        """
        type nums: List[int]
        rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
