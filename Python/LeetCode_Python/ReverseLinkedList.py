#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next
        res = ListNode(None)
        curr = res
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        return res.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next
        res = ListNode(stack.pop())
        curr = res
        while stack:
            if curr.next:
                curr = curr.next
            curr.next = ListNode(stack.pop())
        return res
