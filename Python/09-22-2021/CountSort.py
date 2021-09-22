#!/usr/bin/env python
# coding=utf-8


def countsort_v2(array=[]):
    max_value = array[0]
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]

        if array[i] < min_value:
            min_value = array[i]

    d = max_value - min_value
    count_array = [0] * (d+1)
    for i in range(0, len(array)):
        count_array[array[i] - min_value] += 1

    for i in range(1, len(array)):
        count_array[i] += count_array[i-1]

    sorted_array = [0] * len(array)
    for i in range(len(array)-1, -1, -1):
        sorted_array[count_array[array[i]-min_value]-1] = array[i]
        count_array[array[i] - min_value] -= 1

    return sorted_array


my_array = list([95, 94, 91, 98, 99, 90, 99, 93, 91, 92])
print(countsort_v2(my_array))
