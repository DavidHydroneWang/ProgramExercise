#!/usr/bin/env python
# coding=utf-8
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            i = nums.index(target)
            #print(index)
            return i
        except Exception as e:
            #print(e)
            if target < min(nums):
                return 0
            elif target > max(nums):
                return len(nums)
            else:
                for i in range(len(nums)):
                    if target < nums[i]:
                        #print(i)
                        return i


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        ans = n
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        import bisect
        return bisect.bisect_left(nums, target)
