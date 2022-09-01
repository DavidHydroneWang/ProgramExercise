#!/usr/bin/env python
# coding=utf-8
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)

        for i, side in enumerate(A[:-2]):
            if side < A[i + 1] + A[i + 2]:
                return side + A[i + 1] + A[i + 2]

        return 0



class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        return ([0] + [a + b + c for a, b, c in zip(A, A[1:], A[2:]) if c < a + b])[-1]


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in reversed(range(len(A) - 2)):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
