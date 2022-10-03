#!/usr/bin/env python
# coding=utf-8
class MyStack:

    def __init__(self):

        self.pushQueue = collections.deque()
        self.popQueue = collections.deque()
    def push(self, x: int) -> None:
        self.pushQueue.append(x)
        while self.popQueue:
            self.pushQueue.append(self.popQueue.popleft())
        self.pushQueue, self.popQueue = self.popQueue, self.pushQueue

    def pop(self) -> int:
        return self.popQueue.popleft()

    def top(self) -> int:
        return self.popQueue[0]

    def empty(self) -> bool:
        return not self.popQueue


class MyStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.curr_top = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue2.append(x)
        self.curr_top = x
        while len(self.queue1):
            self.queue2.append(self.queue1.pop(0))
        temp = self.queue2
        self.queue2 = self.queue1
        self.queue1 = temp

    def pop(self):
        """
        :rtype: nothing
        """
        temp = self.queue1.pop(0)
        if len(self.queue1):
            self.curr_top = self.queue1[0]
        return temp

    def top(self):
        """
        :rtype: int
        """
        if self.empty() is False:
            return self.curr_top

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0
