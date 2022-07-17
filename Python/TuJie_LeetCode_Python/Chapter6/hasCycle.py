#!/usr/bin/env python
# coding=utf-8



class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast = head
        slow = head
        while fast:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return False
            if fast is None or slow is None:
                return False
            if fast == slow:
                return True
