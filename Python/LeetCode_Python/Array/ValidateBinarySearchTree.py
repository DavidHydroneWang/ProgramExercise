#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.isValidSub(root, float('-inf'), float('inf'))


    def isValidSub(self, root, minValue, maxValue):
        #print(root)
        if root is None:
            return True

        if root.left is None and root.right is None:
            return minValue < root.val < maxValue
        if root.val <= minValue or root.val >= maxValue:
            return False
        leftsub = self.isValidSub(root.left, minValue, root.val)
        rightsub = self.isValidSub(root.right, root.val, maxValue)
        return leftsub and rightsub


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, node, lower, upper):    # node.val must be above lower and below upper
        if not node:
            return True
        if node.val <= lower or node.val >= upper:  # can be amended if equal values are allowed
            return False
        return self.valid(node.left, lower, node.val) and self.valid(node.right, node.val, upper)
