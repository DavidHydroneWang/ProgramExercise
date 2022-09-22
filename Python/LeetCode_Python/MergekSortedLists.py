#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from bisect import bisect, insort
        if not lists:
            return None
        stack = []
        for l in lists:
            while l is not None:
                insort(stack, l.val)
                l = l.next
        res = ListNode(None)
        new = res
        while stack:
            new.next = ListNode(stack.pop(0))
            new = new.next
        return res.nex


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        for i in range(len(lists)):
            while lists[i]:
                q += lists[i],
                lists[i] = lists[i].next
        root = cur = ListNode(0)
        for h in sorted(q, key = lambda x: x.val):
            cur.next = cur = h
        return root.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        node = head
        nodes = []
        for l_list in lists:
            while l_list:
                nodes.append(l_list.val)
                l_list = l_list.next
        for val in sorted(nodes):
            node.next = ListNode(val)
            node = node.next
        return head.next
