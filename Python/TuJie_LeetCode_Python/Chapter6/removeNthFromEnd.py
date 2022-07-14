#!/usr/bin/env python
# coding=utf-8


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: :ListNode
        """
        pointer = head
        length = 0
        while pointer:
            pointer = pointer.next
            length += 1
        if length == 1:
            return None
        pointer = head
        if n >= length:
            head.val = head.next.val
            head.next = head.next.next
        else:
            if n == 1:
                for i in range(length - 2):
                    pointer = pointer.next
                pointer.next = None
            else:
                for i in range(length - n - 1):
                    pointer = pointer.next
                pointer.next = pointer.next.next
        return head


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: :ListNode
        """
        if head.next is None:
            return None
        left = right = head
        si = 0
        while si < n:
            si += 1
            right = right.next
        if right is None:
            head = head.next
            return head
        while right.next is not None:
            left = left.next
            right = right.next
        if n == 1:
            left.next = None
        else:
            left.next = left.next.next
        return head
