#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                self.tree.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


    def insert(self, v: int) -> int:
        pid = (len(self.tree) - 1) >> 1
        node = TreeNode(v)
        self.tree.append(node)
        p = self.tree[pid]
        if p.left is None:
            p.left = node
        else:
            p.right = node
        return p.val


    def get_root(self) -> TreeNode:
        return self.tree[0]


    def __init__(self, root: TreeNode):
        self.queue = [root]
        self.nodelist = [None]

        while self.queue:
            node = self.queue.pop(0)
            self.nodelist.append(node)
            if node.left:
                self.queue.append(node.left)
            if node.right:
                self.queue.append(node.right)


    def insert(self, v: int) -> int:
        self.nodelist.append(TreeNode(v))
        index = len(self.nodelist) - 1
        father = self.nodelist[index // 2]
        if index % 2 == 0:
            father.left = self.nodelist[-1]
        else:
            father.right = self.nodelist[-1]
        return father.val


    def get_root(self) -> TreeNode:
        return self.nodelist[1]
