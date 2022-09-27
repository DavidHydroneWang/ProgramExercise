#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def maxDepth(root):
            if not root:
                return 0

            leftHeight = maxDepth(root.left)
            if leftHeight == -1:
                return -1
            rightHeight = maxDepth(root.right)
            if rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        return maxDepth(root) != -1


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) >= 0

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: TreeNode) -> int:
            if root == None:
                return False
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight-rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight)+1
        return height(root) >= 0
