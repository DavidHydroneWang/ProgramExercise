#!/usr/bin/env python
# coding=utf-8
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        mydict = {}
        for i in leftChild:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] += 1

        for i in rightChild:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] += 1
        #print(mydict)
        if 0 in mydict:
            return False
        res = True
        for i in mydict.keys():
            if i != -1:
                #print(mydict[i])
                res = res and (mydict[i] == 1)

        for i in range(1, n):
            if i not in mydict.keys():
                return False

        return res



class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        queue = []
        length = 0
        visited = set()
        nodes = set(leftChild + rightChild)
        for x in range(n):
            if x not in nodes:
                queue.append(x)
                break
        else:
            queue.append(0)
        while queue:
            i = queue.pop(0)
            if i != -1 and i not in visited:
                length += 1
                visited.add(i)
                queue.append(leftChild[i])
                queue.append(rightChild[i])
            elif i == -1:
                continue
            else:
                return False
        return length == n


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        roots = set(range(n)) - set(leftChild) - set(rightChild)
        if len(roots) != 1:
            return False
        root, = roots
        stk = [root]
        lookup = set([root])
        while stk:
            node = stk.pop()
            for c in (leftChild[node], rightChild[node]):
                if c < 0:
                    continue
                if c in lookup:
                    return False
                lookup.add(c)
                stk.append(c)
        return len(lookup) == n
