#!/usr/bin/env python
# coding=utf-8
class Solution: 20 / 52 test cases passed.  Time Limit Exceeded
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            try:
                j = nums.index(nums[i], i + 1)
                if abs(j - i) <= k:
                    return True
            except Exception as e:
                pass
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for i in nums:
            if not i in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        for i in range(len(nums)):
            if not my_dict[nums[i]] == 1:
                try:
                    j = nums.index(nums[i], i + 1)
                    if abs(j - i) <= k:
                        return True
                except Exception as e:
                    pass
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])
            if len(nums_set) > k:
                nums_set.remove(nums[i-k])
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                if i - d[num][-1] <= k:
                    return True
                d[num].append(i)
            else:
                d[num] = [i]
        return False
