#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next

        stack.pop(-n)
        #print(stack)
        res = ListNode(None)
        curr = res
        while stack:
            curr.next = ListNode(stack.pop(0))
            curr = curr.next

        return res.next
