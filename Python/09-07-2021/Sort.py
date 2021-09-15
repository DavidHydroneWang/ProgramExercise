#!/usr/bin/env python
# coding=utf-8

def findsnallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectsort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = findsnallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr


print (selectsort([5,3,6,2,10]))






