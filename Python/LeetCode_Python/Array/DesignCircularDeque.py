#!/usr/bin/env python
# coding=utf-8
class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.queue.insert(0,value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue.pop(0)
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue.pop()
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[-1]

    def isEmpty(self) -> bool:
        return not self.queue

    def isFull(self) -> bool:
        return len(self.queue) == self.size
