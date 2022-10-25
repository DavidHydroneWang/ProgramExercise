#!/usr/bin/env python
# coding=utf-8
class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.presum = [0] * (n + 1)
        for i in range(n):
            self.presum[i + 1] = self.presum[i] + w[i]


    def pickIndex(self) -> int:
        n = len(self.presum)
        x = random.randint(1, self.presum[-1])
        left, right = 0, n - 2
        while left < right:
            mid = (left + right) >> 1
            if self.presum[mid + 1] >= x:
                right = mid
            else:
                left = mid + 1
        return left


class Solution:

    def __init__(self, w: List[int]):
        self.prefix = list(itertools.accumulate(w))


    def pickIndex(self) -> int:
        return bisect_left(self.prefix, random.random() * self.prefix[-1])
