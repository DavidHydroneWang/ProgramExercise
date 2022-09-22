#!/usr/bin/env python
# coding=utf-8
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        my_dict = defaultdict(int)
        for i in nums:
            my_dict[str(i)] += 1
        res = []
        length = len(nums)
        for key, value in my_dict.items():
            if value > length / 3:
                res.append(int(key))
        return res


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ls = len(nums)
        res = []
        check_value = []
        for i in range(ls):
            if nums[i] in check_value:
                continue
            count = 1
            for j in range(i + 1, ls):
                if nums[i] == nums[j]:
                    count += 1
            if count > ls / 3:
                res.append(nums[i])
            check_value.append(nums[i])
        return res
