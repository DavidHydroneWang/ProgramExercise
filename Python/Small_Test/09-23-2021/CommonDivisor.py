#!/usr/bin/env python
# coding=utf-8


def get_greatest_common_divisor(a, b):
    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        return small
    for i in range(small//2, 1, -1):
        if small % i == 0 and big % i == 0:
            return i
    return 1


print(get_greatest_common_divisor(25, 5))
print(get_greatest_common_divisor(100, 75))
print(get_greatest_common_divisor(99, 55))
