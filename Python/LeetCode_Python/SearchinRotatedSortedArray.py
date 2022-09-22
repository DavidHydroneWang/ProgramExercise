#!/usr/bin/env python
# coding=utf-8
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        pivot = 0
        length = len(nums)
        while nums[-1] < nums[0]:
            nums = nums[-1:] + nums[:length-1]
            pivot += 1
        #print(pivot)
        pivot %= length
        left, right = 0, length - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                if pivot:
                    if middle - pivot > 0:
                        return (middle - pivot ) % length
                    else:
                        return (middle + length - pivot) % length
                else:
                    return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:  # nums[l..m] are sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # nums[m..n - 1] are sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif sum((target < nums[l], nums[l] <= nums[mid], nums[mid] < target)) == 2:
                l = mid + 1
            else:
                r = mid - 1
        return -1
