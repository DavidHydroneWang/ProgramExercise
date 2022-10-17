#!/usr/bin/env python
# coding=utf-8
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def dfs(self, node: 'Node'):
        # 找到链表的尾节点或 child 链表不为空的节点
        while node.next and not node.child:
            node = node.next
        tail = None
        if node.child:
            # 如果 child 链表不为空，将 child 链表扁平化
            tail = self.dfs(node.child)

            # 将扁平化的 child 链表链接在该节点之后
            temp = node.next
            node.next = node.child
            node.next.prev = node
            node.child = None
            tail.next = temp
            if temp:
                temp.prev = tail
            # 链接之后，从 child 链表的尾节点继续向后处理链表
            return self.dfs(tail)
        # child 链表为空，则该节点是尾节点，直接返回
        return node
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        self.dfs(head)
        return head


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr:
            if curr.child:
                cachedNext = curr.next
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                tail = curr.next
                while tail.next:
                    tail = tail.next
                tail.next = cachedNext
                if cachedNext:
                    cachedNext.prev = tail
            curr = curr.next

        return head


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def flatten(head: 'Node', rest: 'Node') -> 'Node':
            if not head:
                return rest

            head.next = flatten(head.child, flatten(head.next, rest))
            if head.next:
                head.next.prev = head
            head.child = None
            return head

        return flatten(head, None)


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        dummy = Node()
        tail = dummy

        def preOrder(node: 'Node'):
            nonlocal tail
            if node is None:
                return
            next = node.next
            child = node.child
            tail.next = node
            node.prev = tail
            tail = tail.next
            node.child = None
            preOrder(child)
            preOrder(next)

        preOrder(head)
        dummy.next.prev = None
        return dummy.next
