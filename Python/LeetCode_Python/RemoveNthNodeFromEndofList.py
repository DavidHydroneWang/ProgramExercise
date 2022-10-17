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


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        temp = head
        sumall = 0
        while temp is not None:
            sumall += 1
            temp = temp.next
        target = sumall - n - 1
        if target < 0:
            return head.next
        res = head
        for i in range(sumall):
            if i == target:
                res.next = res.next.next
                break
            res = res.next

        return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
