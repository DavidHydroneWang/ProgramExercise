#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            if head.val == val:
                return head.next
            else:
                return head
        while head:
            if head.val == val:
                #print(head.next)
                return self.removeElements(head.next, val)
            else:
                break

        prev, curr = head, head.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if not head:
            return
        node = head
        while node:
            if node.val == val:
                if node.next:
                    node.val = node.next.val
                    node.next = node.next.next
                    continue
                else:
                    prev.next = None
            if not node.next:
                return head
            prev = node
            node = node.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        prehead = ListNode(-1)
        prehead.next = head
        last, pos = prehead, head
        while pos is not None:
            if pos.val == val:
                last.next = pos.next
            else:
                last = pos
            pos = pos.next
        return prehead.next
