#!/usr/bin/env python
# coding=utf-8
class Solution: # partial results
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        new = intervals[:]
        index = 0
        while index < len(intervals):
            start, end = newInterval[0] - intervals[index][0], newInterval[1] - intervals[index][1]
            if start >= 0 and end >= 0:
                if newInterval[0] > intervals[index][1]:
                    pass
                else:
                    new[index][1] = newInterval[1]
                    temp = index
                    for i in range(index + 1, len(intervals)):
                        if newInterval[1] < intervals[i][0]:
                            break
                        if intervals[i][0] <= newInterval[1] <= intervals[i][1]:
                            new[index][1] = intervals[i][1]
                            temp = i
                            new.remove(intervals[i])
#                            print(new)
                        if  newInterval[1] > intervals[i][1]:
                            temp = i
                            new.remove(intervals[i])
#                            print(new)
                    index = temp + 1
#                    print(index)
                    continue
#                    index += 1
            elif start >= 0 and end <= 0:
                pass
            elif start <= 0 and end >= 0:
                new[index][0] = newInterval[0]
                new[index][1] = newInterval[1]
            elif start <= 0 and end <= 0:
                if newInterval[1] < intervals[index][0]:
                    pass
                else:
                    new[index][0] = newInterval[0]
            if index == len(intervals) - 1:
                if newInterval[0] > intervals[index][1]:
                    new.append(newInterval)
                if newInterval[1] < intervals[0][0]:
                    new.insert(0, newInterval)

                # new.append(newInterval)
            index += 1

        return new

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x: x[0])
        if not intervals:
            return []

        result = []

        head = intervals[0][0]
        tail = intervals[0][1]
        length = len(intervals)

        for x in range(1, length):
            i = intervals[x]
            if tail >= i[0]:
                tail = max(tail, i[1])
            else:
                result.append([head, tail])
                head = i[0]
                tail = i[1]

        result.append([head, tail])

        return result


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = 0, len(intervals) - 1
        while left < len(intervals) and intervals[left][1] < newInterval[0]:
            left += 1

        while right >= 0 and intervals[right][0] > newInterval[1]:
            right -= 1

        if left <= right:
            newInterval[0] = min(newInterval[0], intervals[left][0])
            newInterval[1] = max(newInterval[1], intervals[right][1])

        return intervals[:left] + [newInterval] + intervals[right + 1:]
