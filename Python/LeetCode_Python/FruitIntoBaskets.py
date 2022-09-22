#!/usr/bin/env python
# coding=utf-8
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = []
        kinds = set()
        start = 0
        fruitsum = 0
        while start < len(fruits):
            kinds.add(fruits[start])
            if len(kinds) <= 2:
                if len(kinds) == 1:
                    nextstart = start + 1
                fruitsum += 1
                if start == len(fruits) - 1:
                    res.append(fruitsum)
                    return max(res)
                start += 1
            else:
                res.append(fruitsum)
                fruitsum = 0
                kinds = set()
                start = nextstart
        return max(res)


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = i = 0
        last = collections.defaultdict(int)
        for j, val in enumerate(tree):
            if len(last) == 2 and val not in last:
                pre = min(last.values())
                i = pre + 1
                last.pop(tree[pre])
            last[val] = j
            res = max(res, j - i + 1)
        return res
