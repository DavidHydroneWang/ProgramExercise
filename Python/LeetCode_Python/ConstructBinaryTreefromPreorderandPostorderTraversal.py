#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def createTree(preorder, postorder, n):
            if n == 0:
                return None
            node = TreeNode(preorder[0])
            if n == 1:
                return node
            k = 0
            while postorder[k] != preorder[1]:
                k += 1

            node.left = createTree(preorder[1: k + 2], postorder[: k + 1], k + 1)
            node.right = createTree(preorder[k + 2:], postorder[k + 1: -1], n - k - 2)
            return node

        return createTree(preorder, postorder, len(preorder))


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            root = TreeNode(preorder.pop(0))
            postorder.pop()
            if preorder:
                if preorder[0] == postorder[-1]:
                    root.left = self.constructFromPrePost(preorder, postorder)
                else:
                    l, r = postorder.index(preorder[0]), preorder.index(postorder[-1])
                    root.left = self.constructFromPrePost(preorder[:r], postorder[:l + 1])
                    root.right = self.constructFromPrePost(preorder[r:], postorder[l + 1:])
            return root
