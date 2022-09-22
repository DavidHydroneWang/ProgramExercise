#!/usr/bin/env python
# coding=utf-8
class Solution: # time limit exceeded
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        if n == k:
            return [max(nums)]

        for i in range(0, n - k + 1):
            templist = nums[i:i + k]
            res.append(max(templist))

        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        max_window = []

        for i, num in enumerate(nums):

            while q and nums[q[-1]] < num:
                q.pop()

            q.append(i)

            if q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                max_window.append(nums[q[0]])

        return max_window

class Solution:
    def maxSlidingWindow(self, nums, k):
        cnt, heap, res = collections.Counter(), [], []
        for i, num in enumerate(nums):
            heapq.heappush(heap, -num)
            cnt[num] += 1
            while not cnt[-heap[0]]:
                heapq.heappop(heap)
            if i >= k - 1:
                res.append(-heap[0])
                cnt[nums[i - k + 1]] -= 1
        return res
