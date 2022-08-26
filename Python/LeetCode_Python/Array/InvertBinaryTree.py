#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (root.left is None and root.right is None):
            return root

        if root is not None :
            self.invert(root)
            self.invertTree(root.left)
            self.invertTree(root.right)


        return root

    def invert(self, root):
        #print(root)
        if root is not None:
            root.left, root.right = root.right, root.left


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
 #         self.val = val
 #         self.left = left
 #         self.right = right
  class Solution:
     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
         if not root or (root.left is None and root.right is None):
             return root

         root.left, root.right = root.right, root.left
         self.invertTree(root.left)
         self.invertTree(root.right)
         return root]


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
