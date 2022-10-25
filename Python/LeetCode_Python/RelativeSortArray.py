#!/usr/bin/env python
# coding=utf-8
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in range(len(arr2)):
            while arr2[i] in arr1:
                res.append(arr2[i])
                arr1.remove(arr2[i])

        if arr1:
            res += sorted(arr1)

        return res


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = [0] * 1001
        for x in arr1:
            mp[x] += 1
        i = 0
        for x in arr2:
            while mp[x] > 0:
                arr1[i] = x
                mp[x] -= 1
                i += 1
        for x, cnt in enumerate(mp):
            for _ in range(cnt):
                arr1[i] = x
                i += 1
        return arr1


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {num: i for i, num in enumerate(arr2)}
        arr1.sort(key=lambda x: (mp.get(x, 10000), x))
        return arr1


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key = lambda x: arr2.index(x) if x in arr2 else len(arr2) + x)
