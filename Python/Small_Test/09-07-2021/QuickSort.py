#!/usr/bin/env python
# coding=utf-8
import random
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        index = random.randint(0,len(array))
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,3,4,2,3]))
