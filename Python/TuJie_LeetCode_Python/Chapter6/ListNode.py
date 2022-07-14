#!/usr/bin/env python
# coding=utf-8
#
#
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void
        """
        node.val = node.next.val
        node.next = node.next.next
