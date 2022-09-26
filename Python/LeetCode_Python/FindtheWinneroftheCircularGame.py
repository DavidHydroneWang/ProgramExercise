#!/usr/bin/env python
# coding=utf-8
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [(i + 1) for i in range(n)]
        start = 0

        while len(circle) > 1:
            #print(circle)
            index = (start + k - 1) % len(circle)
            circle.remove(circle[index])
            start = index % len(circle)

        return circle[0]


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        ans = (k + self.findTheWinner(n - 1, k)) % n
        return n if ans == 0 else ans


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # true if i-th friend is left
        friends = [False] * n

        friendCount = n
        fp = 0  # friends' pointer

        while friendCount > 1:
            for _ in range(k):
                while friends[fp % n]:  # the friend is not there
                    fp += 1  # point to the next one
                fp += 1
            friends[(fp - 1) % n] = True
            friendCount -= 1

        fp = 0
        while friends[fp]:
            fp += 1

        return fp + 1
