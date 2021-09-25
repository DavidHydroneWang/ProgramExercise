#!/usr/bin/env python
# coding=utf-8


def remove_k_digit(num, k):
    for i in range(0, k):
        has_cut = False
        for j in range(0, len(num)-1):
            if num[j] > num[j+1]:
                num = num[0:j]+num[j+1:len(num)]
                has_cut = True
                break

        if not has_cut:
            num = num[0:len(num)-1]

    for j in range(0, len(num)-1):
        if num[0] != '0':
            break
        num = num[1:len(num)]
    if len(num) == 0:
        return "0"
    return num


print(remove_k_digit("1593212", 3))
print(remove_k_digit("30200", 1))
print(remove_k_digit("10", 2))
print(remove_k_digit("541270936", 3))
print(remove_k_digit("1593212", 4))
