#!/usr/bin/env python
# coding=utf-8
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node

        res = head
        while True:
            if (
                res.val <= insertVal and insertVal <= res.next.val
                or res.val > res.next.val and ( insertVal <= res.next.val or insertVal >= res.val)
                or res.next == head
            ):

                node.next = res.next
                res.next = node
                break
            res = res.next
        return head


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        prev, curr = head, head.next
        while curr != head:
            if prev.val <= insertVal <= curr.val or (
                prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val)
            ):
                break
            prev, curr = curr, curr.next
        prev.next = node
        node.next = curr
        return head

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        node = head
        while node.next != head:
            if node.val <= insertVal <= node.next.val:
                break
            elif node.next.val < node.val <= insertVal:
                break
            elif insertVal < node.next.val < node.val:
                break
            else:
                node = node.next

        insert_node = Node(insertVal)
        insert_node.next = node.next
        node.next = insert_node
        return head
