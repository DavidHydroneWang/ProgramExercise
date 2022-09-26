#!/usr/bin/env python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = [root]

        while q:
            level = []

            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            #print(level)
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]

        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root  # the node just above current needling

        while node:
            dummy = Node(0)  # dummy node before needling
            # needle children of node
            needle = dummy
            while node:
                if node.left:  # needle left child
                    needle.next = node.left
                    needle = needle.next
                if node.right:  # needle right child
                    needle.next = node.right
                    needle = needle.next
                node = node.next
            node = dummy.next  # move node to the next level

        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
