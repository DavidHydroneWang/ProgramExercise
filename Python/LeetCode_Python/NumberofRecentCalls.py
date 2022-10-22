#!/usr/bin/env python
# coding=utf-8
class RecentCounter:

    def __init__(self):
        self.data = []


    def ping(self, t: int) -> int:
        self.data.append(t)
        res = 0

        for i in self.data:
            if   t - 3000 <= i  <= t:
                res += 1
            #else:
                #self.data.remove(i)
        self.data = self.data[len(self.data) - res:]

        return res



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


class RecentCounter:

    def __init__(self):
        self.q = deque()


    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        i = 0
        self.queue.append(t)
        while self.queue[i] < t - 3000:
            i += 1
        self.queue = self.queue[i:]
        return len(self.queue)
