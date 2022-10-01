#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def createTree(preorder, inorder, n):
            if n == 0:
                return None
            k = 0
            while preorder[0] != inorder[k]:
                k += 1

            node = TreeNode(inorder[k])
            node.left = createTree(preorder[1: k + 1], inorder[0:k], k)
            node.right = createTree(preorder[k + 1:], inorder[k + 1:], n - k - 1)

            return node

        return createTree(preorder, inorder, len(inorder))


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[0:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(inorder) == 0:
            return None
        rootIdxIntoInorder = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:], inorder[:rootIdxIntoInorder])
        root.right = self.buildTree(preorder[rootIdxIntoInorder + 1:], inorder[rootIdxIntoInorder + 1:])
        return root
