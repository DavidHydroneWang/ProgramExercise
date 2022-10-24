#!/usr/bin/env python
# coding=utf-8
class MyCalendar:

    def __init__(self):
        self.stack = []


    def book(self, start: int, end: int) -> bool:
        if not self.stack:
            self.stack.append([start, end])
            self.stack.sort()
            return True
        else:
            for date in self.stack:
                if date[0] <= start < date[1] or  date[0] < end <= date[1]  or (start < date[0] and date[1] <=end ):
                    return False
            self.stack.append([start, end])
            self.stack.sort()
            return True


class MyCalendar:

    def __init__(self):
        self.timeline = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.timeline:
            if max(start, s) < min(end, e):
                return False
        self.timeline.append((start, end))
        return True


from sortedcontainers import SortedDict


class MyCalendar:
    def __init__(self):
        self.sd = SortedDict()

    def book(self, start: int, end: int) -> bool:
        idx = self.sd.bisect_right(start)
        if 0 <= idx < len(self.sd):
            if end > self.sd.values()[idx]:
                return False
        self.sd[end] = start
        return True
