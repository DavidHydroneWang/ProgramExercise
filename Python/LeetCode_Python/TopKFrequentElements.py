#!/usr/bin/env python
# coding=utf-8
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from sortedcontainers import SortedDict
        dic = SortedDict()
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        keys = list(dic.values())
        keys.sort(reverse=True)
        keys = keys[:k]

        res = []


        for q in dic:

            if len(res) < k:
                if dic[q] in keys:
                    res.append(q)

        return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        hp = []
        for num, freq in counter.items():
            if len(hp) == k:
                heappush(hp, (freq, num))
                heappop(hp)
            else:
                heappush(hp, (freq, num))
        return [t[1] for t in hp]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in Counter(nums).items():
            bucket[freq].append(num)

        for b in reversed(bucket):
            ans += b
            if len(ans) == k:
                return ans
