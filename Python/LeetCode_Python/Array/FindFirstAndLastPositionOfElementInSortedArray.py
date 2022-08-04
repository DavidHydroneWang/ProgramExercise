#!/usr/bin/env python
# coding=utf-8


class Solution:
    def find_right(self, nums, target):
        lo = 0
        hi = len(nums)
        equals = []
        while lo < hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                equals.append(mid)
            if target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return equals[-1] if equals else -1

    def find_left(self, nums, target):
        lo = 0
        hi = len(nums)
        equals = []
        while lo < hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                equals.append(mid)
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return equals[-1] if equals else -1

    def searchRange(self, nums, target):
        left = self.find_left(nums, target)
        if left == -1:
            return [-1, -1]

        return [left, self.find_right(nums, target)]


class Solution:
    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        startIndex, endIndex = -1, -1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                startIndex, endIndex = mid, mid
                while startIndex > left:
                    leftmid = (left + startIndex) // 2
                    if nums[leftmid] < target:
                        left = leftmid + 1
                    else:
                        startIndex = leftmid
                while endIndex < right:
                    rightmid = (right + endIndex + 1) // 2
                    if nums[rightmid] > target:
                        right = rightmid - 1
                    else:
                        endIndex = rightmid
                return [startIndex, endIndex]
        return [startIndex, endIndex]


slo = Solution()
nums = [1, 2, 2, 2, 3]
target = 2
print(slo.searchRange(nums, target))
