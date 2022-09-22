#!/usr/bin/env python
# coding=utf-8
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        residue = sum(nums) % p
        if not residue:
            return 0
        result = len(nums)
        curr, lookup = 0, {0: -1}
        for i, num in enumerate(nums):
            curr = (curr+num) % p
            lookup[curr] = i
            if (curr-residue) % p in lookup:
                result = min(result, i-lookup[(curr-residue)%p])
        return result if result < len(nums) else -1
