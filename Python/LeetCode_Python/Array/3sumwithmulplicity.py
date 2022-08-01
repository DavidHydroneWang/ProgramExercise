#!/usr/bin/env python
# coding=utf-8


class Solution:
    def threeSumMulti(self, Array, target):
        """
        :type Array: List[int]
        :type target: int
        :rtype: int
        """
        mod = 10**9 + 7

        def get_multiple(time, all_times):
            if time == 1:
                return all_times
            elif time == 2:
                return sum(range(all_times))
            else:
                return sum(plus[:all_times])

        x = {}
        for j in set(Array):
            x[j] = Array.count(j)

        maxes = max(x, key=lambda t: x[t])
        plus = [sum(range(i)) for i in range(x[maxes])]

        Array = []
        for i in sorted(x.keys()):
            if x[i] > 3:
                Array.extend([i]*3)
            else:
                Array.extend([i] * x[i])

        result = 0
        length = len(Array) - 1
        sets = set()
        for i in range(length):
            t = target - Array[i]
            start = i + 1
            end = length

            while start < end:
                if Array[start] + Array[end] == t:
                    _ = [Array[i], Array[start], Array[end]]
                    y = {e: _.count(e) for e in set(_)}

                    _ = "{}{}".format(*_)
                    if _ in sets:
                        start += 1
                        continue

                    c = 1
                    for g in y:
                        c *= get_multiple(y[g], x[g])
                    result += c
                    sets.add(_)
                    start += 1

                if Array[start] + Array[end] > t:
                    end -= 1
                else:
                    start += 1
        return result % mod
