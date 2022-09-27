#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                break
            q.append(node.left)
            q.append(node.right)

        return all(node is None for node in q)


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfsLevelOrder = [root]
        currentIdx = 0
        while bfsLevelOrder[currentIdx]:
            currentNode = bfsLevelOrder[currentIdx]
            bfsLevelOrder.append(currentNode.left)
            bfsLevelOrder.append(currentNode.right)
            currentIdx += 1
        return not any(bfsLevelOrder[currentIdx:])


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        end = False
        current = [root]
        while current:
            next_level = []
            for node in current:
                if not node:
                    end = True
                    continue
                if end:
                    return False
                next_level.append(node.left)
                next_level.append(node.right)
            current = next_level
        return  True
