#!/usr/bin/env python
# coding=utf-8


def bubble_sort_v1(array=[]):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


def bubble_sort_v2(array=[]):
    for i in range(len(array)-1):
        is_Sorted = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                is_Sorted = False
        if is_Sorted:
            break
def bubble_sort_v3(array=[]):
    las_exchange_index = 0
    sort_border = len(array)-1
    for i in range(len(array)-1):
        is_Sorted = True
        for j in range(sort_border):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                is_Sorted = False
                las_exchange_index = j
        sort_border = las_exchange_index
        if is_Sorted:
            break


my_array = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
bubble_sort_v1(my_array)
print(my_array)
bubble_sort_v2(my_array)
print(my_array)
bubble_sort_v3(my_array)
print(my_array)
