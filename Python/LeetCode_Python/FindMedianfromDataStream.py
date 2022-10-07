#!/usr/bin/env python
# coding=utf-8
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        else:
            heappush(self.max_heap, -heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        return (
            (-self.max_heap[0] + self.min_heap[0]) / 2
            if len(self.max_heap) == len(self.min_heap)
            else self.min_heap[0]
        )


class MedianFinder:

    def __init__(self):
        self.stack = []


    def addNum(self, num: int) -> None:
        self.stack.append(num)

    def findMedian(self) -> float:
        length = len(self.stack)
        self.stack.sort()
        if length % 2:
            return self.stack[length // 2]
        else:
            return (self.stack[length // 2] + self.stack[length // 2 - 1]) / 2
