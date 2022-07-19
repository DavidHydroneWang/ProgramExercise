#!/usr/bin/env python
# coding=utf-8


def climbStair(n):
    stepList = [1, 1, 2]
    i = n
    while i > 2:
        stepList.append(stepList[-1] + stepList[-2])
        i -= 1
    return stepList[n]


class Solution:
    def climbStair(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStair(n - 1) + self.climbStair(n - 2)


if __name__ == '__main__':
    n = 5
    print('Count need %d step' % climbStair(n))
