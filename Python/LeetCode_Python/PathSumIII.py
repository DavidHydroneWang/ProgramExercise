#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def dfs(root, summ):
            if not root:
                return 0
            return (summ == root.val) + dfs(root.left, summ - root.val) + dfs(root.right, summ - root.val)

        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, prefixsum_count, target_sum, cur_sum):
        if not root:
            return 0
        res = 0
        cur_sum += root.val
        res += prefixsum_count.get(cur_sum - target_sum, 0)
        prefixsum_count[cur_sum] = prefixsum_count.get(cur_sum, 0) + 1

        res += self.dfs(root.left, prefixsum_count, target_sum, cur_sum)
        res += self.dfs(root.right, prefixsum_count, target_sum, cur_sum)

        prefixsum_count[cur_sum] -= 1
        return res

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        prefixsum_count = dict()
        prefixsum_count[0] = 1
        return self.dfs(root, prefixsum_count, sum, 0)


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        dic = {}
        def traverse(node, parent):
            if not node: return
            dic[node] = [node.val]
            if node.val == sum: res[0] += 1
            if parent:
                for num in dic[parent]:
                    dic[node].append(num + node.val)
                    if num + node.val == sum: res[0] += 1
            traverse(node.left, node)
            traverse(node.right, node)
        res = [0]
        traverse(root, None)
        return res[0]
