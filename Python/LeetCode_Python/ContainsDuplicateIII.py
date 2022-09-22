#!/usr/bin/env python
# coding=utf-8
class Solution: # 36 / 48 test cases passed. Time Limit Exceeded
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from collections import defaultdict
        res = defaultdict(list)
        for i in range(len(nums) - 1):
            for j in range(i + 1, min(len(nums), i + indexDiff + 1)):
                res[nums[i]].append(abs(nums[j] - nums[i]))
        #print(res)
        for i in res.values():
            if min(i) <= valueDiff:
                return True
        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket_dict = dict()
        for i in range(len(nums)):
            # 将 nums[i] 划分到大小为 t + 1 的不同桶中
            num = nums[i] // (t + 1)

            # 桶中已经有元素了
            if num in bucket_dict:
                return True

            # 把 nums[i] 放入桶中
            bucket_dict[num] = nums[i]

            # 判断左侧桶是否满足条件
            if (num - 1) in bucket_dict and abs(bucket_dict[num - 1] - nums[i]) <= t:
                return True
            # 判断右侧桶是否满足条件
            if (num + 1) in bucket_dict and abs(bucket_dict[num + 1] - nums[i]) <= t:
                return True
            # 将 i-k 之前的旧桶清除，因为之前的桶已经不满足条件了
            if i >= k:
                bucket_dict.pop(nums[i-k] // (t + 1))

        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        d = {}
        for i in range(len(nums)):
            m = nums[i] // (t + 1)
            if m in d or (m - 1 in d and nums[i] - d[m - 1] <= t) or (m + 1 in d and d[m + 1] - nums[i] <= t):
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] // (t + 1)]
        return False
