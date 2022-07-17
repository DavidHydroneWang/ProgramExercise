#!/usr/bin/env python
# coding=utf-8


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype : ListNode
        """
        valList = []
        pointer = head
        while pointer:
            valList.append(pointer.val)
            pointer = pointer.next
        pointer = head
        while valList:
            pointer.val = valList.pop()
            pointer = pointer.next
        retutn head


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype : ListNode
        """
        if head is None:
            retutn None
        left = right = head
        if right.next = None:
            retutn head
        else:
            right = right.next
            left.next = None
        while right is not None:
            head = right
            right = right.next
            head.next = left
            left = head
        return head
