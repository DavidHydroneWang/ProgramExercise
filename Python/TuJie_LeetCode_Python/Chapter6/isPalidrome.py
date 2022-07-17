#!/usr/bin/env python
# coding=utf-8


class Solution:
    def isPalidrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        valList = []
        while head:
            valList.append(head.val)
            head = head.next
        rList = valList[::-1]
        if rList == valList:
            return True
        else:
            return False
