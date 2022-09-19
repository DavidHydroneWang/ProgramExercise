#!/usr/bin/env python
# coding=utf-8
class Solution: # 142 / 161 test cases passed. Time Limit Exceeded
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        greater = float('inf')
        lesser = float('inf')
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right] - target
                if res == 0:
                    return target
                elif res > 0:
                    right -= 1
                    greater = min(greater, abs(res))
                elif res < 0:
                    left += 1
                    lesser = min(lesser, abs(res))

        if greater > lesser:
            return - lesser + target
        else:
            return greater + target





class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        triplate = []
        prevSum = float("-inf")
        prevDiff = target - prevSum
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                currentDiff = target - currentSum
                prevDiff = target - prevSum
                if abs(currentDiff) < abs(prevDiff):
                    triplate = [nums[i], nums[left], nums[right]]
                    prevDiff = currentDiff
                    prevSum = currentSum
                if currentSum < target:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif currentSum > target:
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                else:
                    return sum(triplate[:])
        return sum(triplate[:])



class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')  # default if len(nums) < 3

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:

                triple = nums[i] + nums[j] + nums[k]
                if triple == target:    # early return, cannot do better
                    return target
                if abs(triple - target) < abs(closest - target):
                    closest = triple

                if triple - target > 0:
                    k -= 1
                else:
                    j += 1

        return closest


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if abs(sm - target) < diff: diff, res = abs(sm - target), sm
                if sm < target: l += 1
                elif sm > target: r -= 1
                else: return res
        return res
