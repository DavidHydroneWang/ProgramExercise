#!/usr/bin/env python
# coding=utf-8
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        #print(dir(Counter))
        res = Counter(nums).most_common(1)[0][0]

        return res
