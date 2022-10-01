#!/usr/bin/env python
# coding=utf-8
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = [1]
        my_dict = {}
        for i in primes:
            my_dict[str(i)] = 0


        while len(nums) < n:
            temp = []
            for i in primes:
                nex = nums[ my_dict[str(i)]] * i
                temp.append(nex)

            next = min(temp)
            for i in primes:
                if next == nums[my_dict[str(i)]] * i:
                    my_dict[str(i)] += 1

            nums.append(next)

        return nums[-1]


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        arr, heap, used = [1], primes[:], set()
        for i in range(1, n):
            num = heapq.heappop(heap)
            arr.append(num)
            for p in primes:
                if p * num not in used:
                    heapq.heappush(heap, p * num)
                    used.add(p * num)
        return arr[-1]


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        super_ugly = [1]
        # super_ugly[indices[i]] is the last super_ugly number to be multiplied by primes[i] to generate candidates[i]
        indices = [0 for _ in range(len(primes))]
        candidates = primes[:]

        while len(super_ugly) < n:

            ugly = min(candidates)
            super_ugly.append(ugly)

            for i in range(len(candidates)):    # update all candidates equal to ugly (avoids duplicates)
                if ugly == candidates[i]:
                    indices[i] += 1
                    candidates[i] = primes[i] * super_ugly[indices[i]]

        return super_ugly[-1]

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        nums = [1]
        indices = [0] * k

        while len(nums) < n:
            nexts = [0] * k
            for i in range(k):
                nexts[i] = nums[indices[i]] * primes[i]
            next = min(nexts)
            for i in range(k):
                if next == nexts[i]:
                    indices[i] += 1
            nums.append(next)

        return nums[-1]
