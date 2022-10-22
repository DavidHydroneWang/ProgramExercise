#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        if self.containsOnlyZero(root):
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root
    def containsOnlyZero(self, root: TreeNode):
        if not root:
            return True
        if root.val == 1:
            return False
        return self.containsOnlyZero(root.left) and self.containsOnlyZero(root.right)


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def contains_one(node):

            if not node:
                return False
            left_one, right_one = contains_one(node.left), contains_one(node.right) # explore and prune children

            if not left_one:                                # remove subtrees without 1s
                node.left = None
            if not right_one:
                node.right = None

            return node.val == 1 or left_one or right_one   # 1 in node or subtrees

        return root if contains_one(root) else None         # handle tree with no 1s
