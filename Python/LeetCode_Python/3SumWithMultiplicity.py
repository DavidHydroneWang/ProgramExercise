#!/usr/bin/env python
# coding=utf-8
class Solution: # 39 / 72 test cases passed. Time Limit Exceeded
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        from itertools import combinations as cb
        res = 0
        if len(arr) < 3:
            return res
        #visited = []
        for i, j, k in cb(arr, 3):

            if i + j + k == target:
                res += 1

        return res %  (10 ** 9 + 7)


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        counts = [0] * 101
        for num in arr:
            counts[num] += 1

        result = 0

        for small, small_count in enumerate(counts):
            if small_count == 0:
                continue

            for med, med_count in enumerate(counts[small:], small):
                if med_count == 0:
                    continue

                other = target - small - med
                if other < 0 or other > 100 or counts[other] == 0:
                    continue
                other_count = counts[other]

                if small == med == other:
                    result += small_count * (small_count - 1) * (small_count - 2) // 6
                elif small == med:          # exactly 2 numbers are the same
                    result += small_count * (small_count - 1) * other_count // 2
                elif other > med:           # add if in order (med is always > small)
                    result += small_count * med_count * other_count

        return result % (10 ** 9 + 7)
