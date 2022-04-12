#!/usr/bin/env python
# coding=utf-8


class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, element):
        self.main_stack.append(element)
        if len(self.min_stack) == 0 or\
           element < self.min_stack[len(self.min_stack)-1]:
            self.min_stack.append(element)

    def pop(self):
        if self.main_stack[len(self.main_stack)-1] == \
           self.min_stack[len(self.min_stack)-1]:
            self.min_stack.pop()
        return self.main_stack.pop()

    def get_min(self):
        if len(self.main_stack) == 0:
            return None
        return self.min_stack[len(self.min_stack)-1]


my_stack = MinStack()
my_stack.push(4)
my_stack.push(9)
my_stack.push(7)
my_stack.push(4)
my_stack.push(3)
my_stack.push(8)
my_stack.push(5)
print(my_stack.get_min())
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.get_min())
