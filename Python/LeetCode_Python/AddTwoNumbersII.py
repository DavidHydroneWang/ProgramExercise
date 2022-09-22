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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1)
            l1 = l1.next

        while l2:
            stack2.append(l2)
            l2 = l2.next

        head = None
        carry = 0

        while carry or stack1 or stack2:
            if stack1:
                carry += stack1.pop().val
            if stack2:
                carry += stack2.pop().val
            node = ListNode(carry % 10)
            node.next = head
            head = node
            carry //= 10

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0

        node = l1
        while node:
            num1 = num1 * 10 + node.val
            node = node.next
        node = l2
        while node:
            num2 = num2 * 10 + node.val
            node = node.next

        total = num1 + num2
        if total == 0:              # return single node with zero
            return ListNode(0)
        result = None

        while total:
            total, digit = divmod(total, 10)
            new_node = ListNode(digit)
            new_node.next = result  # make digit start of result
            result = new_node

        return result
