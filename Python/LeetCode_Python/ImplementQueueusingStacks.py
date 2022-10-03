#!/usr/bin/env python
# coding=utf-8
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:

        self.stack1.append(x)
        #self.stack2.append(self.stack1.peek())


    def pop(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()
        top = self.stack2[-1]
        self.stack2.pop()
        return top



    def peek(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()
        top = self.stack2[-1]

        return top


    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
