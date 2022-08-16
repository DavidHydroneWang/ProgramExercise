#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#from collections import defaultdict
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashset = set()
        pos = 0
        hashset.add(head)
        while head is not None:
            head = head.next
            if head is None:
                return None
            if head in hashset:
                return head
            hashset.add(head)
        return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#from collections import defaultdict
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            fast = head.next.next
            slow = head.next

            while fast != slow:
                fast = fast.next.next
                slow = slow.next
        except:
            return None
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
