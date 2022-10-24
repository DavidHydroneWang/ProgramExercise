#!/usr/bin/env python
# coding=utf-8
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stack = nums[:]

    def add(self, val: int) -> int:

        self.stack.append(val)
        self.stack.sort()

        return self.stack[ -self.k ]


import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
