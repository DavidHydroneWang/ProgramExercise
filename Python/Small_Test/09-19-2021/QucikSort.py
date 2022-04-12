#!/usr/bin/env python
# coding=utf-8


def quick_sort(start_index, end_index, array=[]):
    if start_index >= end_index:
        return
    pivot_index = partition_v1(start_index, end_index, array)
    quick_sort(start_index, pivot_index - 1, array)
    quick_sort(pivot_index + 1, end_index, array)


def quick_sort2(start_index, end_index, array=[]):
    if start_index >= end_index:
        return
    pivot_index = partition_v2(start_index, end_index, array)
    quick_sort(start_index, pivot_index - 1, array)
    quick_sort(pivot_index + 1, end_index, array)


def partition_v1(start_index, end_index, array=[]):
    pivot = array[start_index]
    left = start_index
    right = end_index
    while left != right:
        while left < right and array[right] > pivot:
            right -= 1
        while left < right and array[left] <= pivot:
            left += 1
        if left < right:
            p = array[left]
            array[left] = array[right]
            array[right] = p

    array[start_index] = array[left]
    array[left] = pivot
    return left


def partition_v2(start_index, end_index, array=[]):
    pivot = array[start_index]
    mark = start_index
    for i in range(start_index+1, end_index+1):
        if array[i] < pivot:
            mark += 1
            p = array[mark]
            array[mark] = array[i]
            array[i] = p
    array[start_index] = array[mark]
    array[mark] = pivot
    return mark


my_array = list([3, 4, 14, 1, 5, 6, 7, 8, 9, -1, 0, 9, 11])
quick_sort(0, len(my_array)-1, my_array)
print(my_array)
quick_sort2(0, len(my_array)-1, my_array)
print(my_array)
