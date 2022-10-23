#!/usr/bin/env python
# coding=utf-8
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = []
        self.inOrder(root, res)
        print(res)
        for i in range(len(res)):
            try:
                index = res.index(k - res[i])
                if index != i:
                    return True
            except Exception as e:
                pass
        return False

    def inOrder(self, node, res):
        if not node:
            return

        self.inOrder(node.left, res)
        res.append(node.val)
        self.inOrder(node.right, res)


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def find(root):
            if not root:
                return False
            if k - root.val in nodes:
                return True
            nodes.add(root.val)
            return find(root.left) or find(root.right)

        nodes = set()
        return find(root)


class Solution:
    def inOrder(self, root, nums):
        if not root:
            return
        self.inOrder(root.left, nums)
        nums.append(root.val)
        self.inOrder(root.right, nums)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        self.inOrder(root, nums)
        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                return True
            elif sum < k:
                left += 1
            else:
                right -= 1
        return False


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def traverse(node):
            if not node: return False
            if not node.val in dic: dic[k-node.val]=1
            else: return True
            return traverse(node.left) or traverse(node.right)
        dic={}
        return traverse(root)
