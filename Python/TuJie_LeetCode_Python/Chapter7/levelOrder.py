#!/usr/bin/env python
# coding=utf-8


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rList = []
        subList = []
        if not root:
            return rList
        else:
            cNodeList = [root]
        nNodeList = []
        while True:
            if cNodeList:
                node = cNodeList.pop(0)
                subList.append(node.val)
                if node.left and node.right:
                    nNodeList.append(node.left)
                    nNodeList.append(node.right)
                elif node.left:
                    node.append(node.left)
                elif node.right:
                    node.append(node.right)
                else:
                    pass
            else:
                rList.append(subList[:])
                subList = []
                if not nNodeList:
                    break
                else:
                    cNodeList = nNodeList[:]
                    nNodeList = []
        return rList
