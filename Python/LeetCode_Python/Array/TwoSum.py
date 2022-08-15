#!/usr/bin/env python
# coding=utf-8


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, j in enumerate(nums):
            my_dict[str(j)] = i
        print(my_dict)
        for i in range(len(nums)):
            new = target - nums[i]
            try:
                j = my_dict[str(new)]
                if i == j:
                    continue
                else:
                    return [i, j]
                #return [i, j]
            except Exception as e:
                pass
