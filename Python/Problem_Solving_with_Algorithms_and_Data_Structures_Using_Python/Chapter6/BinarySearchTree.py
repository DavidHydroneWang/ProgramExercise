#!/usr/bin/env python
# coding=utf-8


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


class TreeNode:
    def __init__(self, key, val, left=None, right=None,
                 parent=None):
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftchild

    def hasRightChild(self):
        return self.rightchild

    def isLeftChild(self):
        return self.parent and \
                self.parent.leftchild == self

    def isRightChild(self):
        return self.parent and \
                self.parent.rightchild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightchild or self.leftchild)

    def hasAnyChildren(self):
        return self.rightchild or self.leftchild

    def hasBothChildren(self):
        return self.rightchild and self.leftchild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftchild = lc
        self.rightchild = rc
        if self.hasLeftChild():
            self.leftchild.parent = self
        if self.hasRightChild():
            self.rightchild.parent = self

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftchild)
            else:
                currentNode.leftchild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightchild)
            else:
                currentNode.rightchild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, key, val):
        self.put(key, val)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif:
            key < currentNode.key:
                return self._get(key, currentNode.leftchild)
        else:
            return self._get(key, currentNode.rightchild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
