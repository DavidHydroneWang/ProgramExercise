#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tree = set()
        self.transversal(root, tree)
        #print(tree)
        for i in tree:
            #print(i)
            if self.children(i, p)  and self.children(i, q):
                if not (self.children(i.left, p)  and self.children(i.left, q)) and not (self.children(i.right, p)  and self.children(i.right, q)):
                    return i


    def transversal(self, root, tree):
        if root is None:
            return
        tree.add(root)
        self.transversal(root.left,tree)
        self.transversal(root.right, tree)

    def children(self, nodeParent, nodeChildren):
        tree = set()
        self.transversal(nodeParent, tree)
        for i in tree:
            if i == nodeChildren:
                return True
        return False


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if ancestor.val > p.val and ancestor.val > q.val:
                ancestor = ancestor.left
            elif ancestor.val < p.val and ancestor.val < q.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
