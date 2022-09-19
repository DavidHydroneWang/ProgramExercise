#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next
        length = len(stack)
        k = k % length
        if k == 0:
            pass
        else:
            stack = stack[-k:] + stack[:length - k ]

        new = ListNode
        head = new
        while stack:
            head.next = ListNode(stack.pop(0))
            head = head.next
        return new.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head
        curr = head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        cut = count - k % count
        curr.next = head
        while cut:
            curr = curr.next
            cut -= 1
        newHead = curr.next
        curr.next = None
        return newHead
