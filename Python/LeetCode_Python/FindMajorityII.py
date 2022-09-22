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
