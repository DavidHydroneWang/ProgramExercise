#!/usr/bin/env python
# coding=utf-8


def count_sort(array=[]):
    max_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]

    count_array = [0] * (max_value+1)
    for i in range(0, len(array)):
        count_array[array[i]] += 1

    sorted_array = []
    for i in range(0, len(count_array)):
        for j in range(0, count_array[i]):
            sorted_array.append(i)

    return sorted_array


my_array = list([4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10])
print(count_sort(my_array))
