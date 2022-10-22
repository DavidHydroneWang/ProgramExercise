#!/usr/bin/env python
# coding=utf-8
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.data = []


    def next(self, val: int) -> float:
        if len(self.data) == self.size:
            self.data.pop(0)
        self.data.append(val)
        return sum(self.data) / len(self.data)
