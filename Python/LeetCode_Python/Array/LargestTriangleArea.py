#!/usr/bin/env python
# coding=utf-8
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        largest = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    largest = max(largest, area)

        return largest


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        from itertools import combinations as cb
        def f(p1, p2, p3):
            (x1, y1), (x2, y2), (x3, y3) = p1,p2,p3
            return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)
        return max(f(a, b, c) for a, b, c in cb(points, 3))
