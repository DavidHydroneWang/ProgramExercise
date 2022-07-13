#!/usr/bin/env python
# coding=utf-8


class Solution:
    def rotate(self, nums, k):
        """
        type nums: List[int]
        type k: int
        rtype: void
        """
        if len(nums) < 2:
            return
        nums.reverse()
        k = k % len(nums)
        while k > 0:
            temp = nums.pop(0)
            nums.appen(temp)
            k -= 1
        nums.reverse()
        return


class Solution:
    def rotate(self, nums, k):
        """
        type nums: List[int]
        type k: int
        rtype: void
        """
        if len(nums) < 2:
            return
        k = k % len(nums)
        while k > 0:
            temp = nums[-1]
            nums[1:] = nums[:-1]
            nums[0] = temp
            k -= 1
        return


class Solution:
    def rotate(self, nums, k):
        """
        type nums: List[int]
        type k: int
        rtype: void
        """
        if len(nums) < 2:
            return
        k = k % len(nums)
        temp = nums[len(nums) - k:]
        nums[k:] = nums[:len(nums) - k]
        nums[:k] = temp
        return
