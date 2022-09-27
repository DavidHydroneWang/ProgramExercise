#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         sel
class Solution: #  72 / 80 test cases passed. Status: Wrong Answer
    def isValidBST(self, root):
        if not root:
            return
        if root and root.left and root.right:
            if root.left.val < root.val < root.right.val:
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False
        elif root and root.left:
            if root.left.val < root.val:
                 return self.isValidBST(root.left)
            else:
                return False
        elif root and root.right:
            if root.val < root.right.val:
                return self.isValidBST(root.right)
            else:
                return False
        elif root:
            return True


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


class Solution:
    def isValidBST(self, root):
        order = []
        self.validator(root, order)
        for i in range(1, len(order)):
            if order[i-1] >= order[i]:
                return False
        return True

    def validator(self, root, order):
        if not root:
            return 0
        self.validator(root.left, order)
        order.append(root.val)
        self.validator(root.right, order)


class Solution:
    def isValidBST(self, root):
        def preorderTraversal(root, min_v, max_v):
            if root == None:
                return True
            if root.val >= max_v or root.val <= min_v:
                return False
            return preorderTraversal(root.left, min_v, root.val) and preorderTraversal(root.right, root.val, max_v)

        return preorderTraversal(root, float('-inf'), float('inf'))
