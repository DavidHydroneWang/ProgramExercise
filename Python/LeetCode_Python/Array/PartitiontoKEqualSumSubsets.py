#!/usr/bin/env python
# coding=utf-8
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(i, sums): # test whether nums[i] can be added to some sums
            if i == n:
                return True
            for j in range(k):
                if sums[j] + nums[i] <= target:
                    sums[j] += nums[i]
                    if dfs(i + 1, sums):
                        return True
                    sums[j] -= nums[i]
                if sums[j] == 0:
                    break # do not try other empty buckets
            return False
        nums.sort(reverse = True)
        sm = sum(nums)
        if sm % k: return False
        target, n = sm // k, len(nums)
        return dfs(0, [0] * k)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        nums.sort(reverse = True)
        target = total // k
        if total % k != 0 or nums[0] > target:
            return False

        partition = [0 for _ in range(k)]

        def helper(i):                          # test whether nums[i] can be added to some partition
            if i == len(nums):
                return True

            for j in range(len(partition)):
                if partition[j] + nums[i] <= target:
                    partition[j] += nums[i]
                    if helper(i + 1):
                        return True
                    partition[j] -= nums[i]
                if partition[j] == 0:           # do not try other empty buckets
                    break

            return False

        return helper(0)
