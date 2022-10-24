#!/usr/bin/env python
# coding=utf-8
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import heappush, heappop
        hp = []

        for x in nums1[:k]:
            for y in nums2[:k]:
                if len(hp) < k:
                    heappush(hp, ( -(x + y), [x, y]))
                else:
                    if (x + y) < -hp[0][0]:
                        heappop(hp)
                        heappush(hp, (-(x + y), [x, y]))
                    else:
                        break

        return [p for _, p in hp]

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import  heapq
        maxHeap = []
        for nums1Idx in range(min(k, len(nums1))):
            for nums2Idx in range(min(k, len(nums2))):
                currentPairSum = nums1[nums1Idx] + nums2[nums2Idx]
                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, (-currentPairSum, nums1Idx, nums2Idx))
                else:
                    if currentPairSum < (-maxHeap[0][0]):
                        heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap, (-currentPairSum, nums1Idx, nums2Idx))
                    else:
                        break
        smallestPairs = []
        for (currentPairSum, nums1Idx, nums2Idx) in maxHeap:
            smallestPairs.append([nums1[nums1Idx], nums2[nums2Idx]])
        return smallestPairs


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        n, res, cnt, heap = len(nums2), [], 0, [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        while heap and cnt < k:
            cnt += 1
            sm, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n: heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
