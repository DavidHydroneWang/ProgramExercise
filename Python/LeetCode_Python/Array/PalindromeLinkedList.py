#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        return stack == stack[::-1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        i, j = 0, len(stack) - 1
        while i <= j:
            if stack[i] != stack[j]:
                return False
            i += 1
            j -= 1
        return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        r = fast = head
        l = None
        while fast and fast.next:
            fast = fast.next.next
            r.next, l, r = l, r, r.next
        if fast: r = r.next
        while l and r and l.val == r.val:
            l, r = l.next, r.next
        return not l
