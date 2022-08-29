#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #if root is None:
            #return False
        res = []
        self.hasPath(root, targetSum, res)

        #print(res)
        return any(res)

    def hasPath(self, root, targetSum, res) :
        if root is None:
            return False
        if root is not None:
            if root.left is  None and root.right is  None:
                res.append(self.hasTarget(root, targetSum))
            self.hasPath(root.left, targetSum - root.val, res)
            self.hasPath(root.right, targetSum - root.val, res)


    def hasTarget(self, root, target):

        if root.val == target:
            return True
        else:
            return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        targetSum -= root.val
        if targetSum == 0 and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
