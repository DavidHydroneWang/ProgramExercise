#!/usr/bin/env python
# coding=utf-8
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        length = len(original)
        if length != n * m:
            return res
        for i in range(m):
            #for j in range(n):
            res.append(original[i * n: i * n + n ])

        return res


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        return [original[i : i + n] for i in range(0, m * n, n)]


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        ans = [[0] * n for _ in range(m)]

        for i, num in enumerate(original):
            ans[i // n][i % n] = num

        return ans
