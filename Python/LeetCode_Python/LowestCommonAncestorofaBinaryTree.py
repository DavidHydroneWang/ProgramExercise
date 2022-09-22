#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # 29 / 31 test cases passed. Status: Time Limit Exceeded
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
        if root == p or root == q:
            return root

        if root:
            node_left = self.lowestCommonAncestor(root.left, p, q)
            node_right = self.lowestCommonAncestor(root.right, p, q)
            if node_left and node_right:
                return root
            elif not node_left:
                return node_right
            else:
                return node_left
        return None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent, stack = {root: None}, [root]
        while p not in parent or q not in parent: # iterate until we find both p and q
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set() # p's ancestors
        while p:
            ancestors.add(p)
            p = parent[p] # p becomes None in the end
        # go up from q until meet any of p's ancestors
        while q not in ancestors:
            q = parent[q]
        return q
