#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = []
        self.inOrder(root,res)

        for i in range(len(res)):
            if res[i] == p:
                try:
                    return res[i + 1]
                except Exception as e:
                    return None

        return None

    def inOrder(self, node, res):
        if not node:
            return

        self.inOrder(node.left,res)
        res.append(node)
        self.inOrder(node.right,res)


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        cur, ans = root, None
        while cur:
            if cur.val <= p.val:
                cur = cur.right
            else:
                ans = cur
                cur = cur.left
        return ans
