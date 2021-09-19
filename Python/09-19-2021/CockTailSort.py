#!/usr/bin/env python
# coding=utf-8


def cock_tail_sort(array=[]):
    for i in range(len(array) // 2):
        is_Sorted = True
        for j in range(i, len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                is_Sorted = False

        if is_Sorted:
            break

        is_Sorted = True
        for j in range(len(array)-i-1, i, -1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                is_Sorted = False

        if is_Sorted:
            break


my_array = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
cock_tail_sort(my_array)
print(my_array)
