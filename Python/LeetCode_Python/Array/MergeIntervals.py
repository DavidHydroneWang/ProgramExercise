#!/usr/bin/env python
# coding=utf-8
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        if not intervals or (len(intervals) == 1 and len(intervals[0]) < 3):
            return intervals

        remo = []
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:

                remo.append(intervals[i])
                intervals[i + 1] = [intervals[i][0], max(intervals[i + 1][1], intervals[i][1])]
                i += 1
            else:

                i += 1

        while remo:
            index = remo.pop(0)
            intervals.remove(index)
        return intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][-1]:
                intervals[i-1] = [min(intervals[i][0], intervals[i-1][0]), max(intervals[i][-1], intervals[i-1][-1])]
                intervals.pop(i)
            else:
                i += 1
        return intervals
