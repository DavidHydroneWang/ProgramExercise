#!/usr/bin/env python
# coding=utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number = 0
        stack = 0
        number += self.LinkedListToInteger(l1)
        number += self.LinkedListToInteger(l2)
        if number == 0:
            stack.append(0)
        while number:
            stack.append(number % 10)
            number //= 10
        l3 = ListNode(stack.pop())
        node = l3
        while stack:
            node.next = ListNode(stack.pop())
            node = node.next
        return l3

    def LinkedListToInteger(l):
        n = 0
        while l:
            n = n * 10 + l.val
            l = l.next
        return n
