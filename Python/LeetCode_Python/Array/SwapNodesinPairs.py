#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = ListNode(None)
        curr = head
        nex = curr.next
        res = nex
        while nex:
            prev.next = nex
            curr.next = nex.next
            nex.next = curr

            try:
                prev = curr
                curr = curr.next
                nex = curr.next

            except Exception as e:
                curr = nex.next
                nex = None


        return res


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        first = head.next
        second = head
        second.next = self.swapPairs(first.next)
        first.next = second
        return first

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head
        head.val, head.next.val = head.next.val, head.val
        if head.next.next:
            self.swapPairs(head.next.next)
        return head
