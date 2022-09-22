#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if root is None:
            return res

        if targetSum == root.val and root.left is None and root.right is None:
            return [[root.val]]

        left_res = self.pathSum(root.left, targetSum - root.val)
        right_res = self.pathSum(root.right, targetSum - root.val)


        for i in left_res + right_res:
            res.append([root.val] + i)

        return res


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        resultCache, currentPath = [], []
        self.pathSumHelper(root, targetSum, currentPath, resultCache)
        return resultCache

    def pathSumHelper(self, root, targetSum, currentPath, resultCache):
        if root:
            currentPath.append(root.val)
            if not root.left and not root.right:
                if root.val == targetSum:
                    resultCache.append(list(currentPath))
            if root.left:
                self.pathSumHelper(root.left, targetSum - root.val, currentPath, resultCache)
            if root.right:
                self.pathSumHelper(root.right, targetSum - root.val, currentPath, resultCache)
            currentPath.pop()


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traverse(node, q, residue, res = []):
            if node:
                if not node.left and not node.right and residue + node.val == targetSum: res.append(q + [node.val])
                traverse(node.left, q + [node.val], residue + node.val)
                traverse(node.right, q + [node.val], residue + node.val)
            return res
        return traverse(root, [], 0)
