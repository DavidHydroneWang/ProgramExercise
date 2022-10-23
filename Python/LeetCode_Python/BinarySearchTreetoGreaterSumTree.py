#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        self.inOrder(root, res)
        #print(res)
        ans = res[:]
        #print(ans)

        for i in range(len(res)- 2, -1, -1):
            res[i] += res[i + 1]
        #print(res)
        my_dict = dict()
        for key, val in zip(ans, res):
            my_dict[key] = val
        #print(my_dict)
        self.inOrder2(root, my_dict)
        return root

    def inOrder(self, node, res):
        if not node:
            return

        self.inOrder(node.left, res)
        #res[node] = node.val
        res.append(node.val)
        self.inOrder(node.right, res)

    def inOrder2(self, node, my_dict):
        if not node:
            return
        self.inOrder2(node.left, my_dict)
        if node.val in my_dict.keys():
            node.val = my_dict[node.val]
        self.inOrder2(node.right, my_dict)


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            nonlocal s
            if root is None:
                return
            dfs(root.right)
            s += root.val
            root.val = s
            dfs(root.left)

        s = 0
        dfs(root)
        return root
