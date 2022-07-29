#!/usr/bin/env python
# coding=utf-8


class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insertLeft(self, node):
        if self.left is None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t

    def insertRight(self, node):
        if self.right is None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRootValue(self, obj):
        self.key = obj

    def getRootValue(self):
        return self.key
