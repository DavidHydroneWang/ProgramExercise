#!/usr/bin/env python
# coding=utf-8


class Solution:
    def numSubarrayWithSum(self, Array, Sum):
        dicts = {0: 1}
        pre = 0
        result = 0
        for i in Array:
            pre += i
            result += dicts.get(pre - Sum, 0)
#            print(result)
            dicts[pre] = dicts.get(pre, 0) + 1

        return result


A = [1, 0, 1, 0, 1]
S = 2
res = Solution()
print(res.numSubarrayWithSum(A, S))
