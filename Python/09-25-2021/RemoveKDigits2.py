#!/usr/bin/env python
# coding=utf-8


def remove_k_digits_v2(num, k):
    new_length = len(num) - k
    stack = []
    for i in range(0,len(num)):
        c = num[i]
        while len(stack) > 0 and stack[len(stack)-1] > c and k > 0:
            stack.pop()
            k -= 1

        if '0' == c and len(stack) == 0:
            new_length -= 1
            if new_length <= 0:
                return "0"
            continue
        stack.append(c)

    if new_length <= 0:
        return "0"
    return "".join(stack)


print(remove_k_digits_v2("1593213", 3))
print(remove_k_digits_v2("30200", 1))
print(remove_k_digits_v2("1593213", 4))
