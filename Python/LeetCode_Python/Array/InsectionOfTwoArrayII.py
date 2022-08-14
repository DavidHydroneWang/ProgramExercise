#!/usr/bin/env python
# coding=utf-8
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        inter = list(set(nums1) & set(nums2))

        for i in inter:
            length1 = nums1.count(i)
            length2 = nums2.count(i)
            if length1 <= length2:
                while i in nums1:
                    result.append(i)
                    nums1.remove(i)
            else:
                while i in nums2:
                    result.append(i)
                    nums2.remove(i)
        return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []

        for key in count1:
            if key in count2:
                minFreq = min(count1[key], count2[key])
                for i in range(minFreq):
                    result.append(key)

        return result
