#!/usr/bin/env python
# coding=utf-8


def up_adjust(array=[]):
    child_index = len(array) - 1
    parent_index = (child_index - 1) // 2
    temp = array[child_index]
    while child_index > 0 and temp < array[parent_index]:
        array[child_index] = array[parent_index]
        child_index = parent_index
        parent_index = (parent_index - 1) // 2
    array[child_index] = temp


def down_adjust(parent_index, length, array=[]):
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        if child_index + 1 < length and \
           array[child_index + 1] < array[child_index]:
            child_index += 1
        if temp <= array[child_index]:
            break
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * child_index + 1
    array[parent_index] = temp


def build_heap(array=[]):
    for i in range((len(array) - 2) // 2, 1, -1):
        down_adjust(i, len(array), array)


my_array = list([1, 3, 2, 6, 5, 7, 8, 9, 10, 0])
up_adjust(my_array)
print(my_array)
my_array = list([7, 1, 3, 10, 5, 2, 8, 9, 6])
build_heap(my_array)
print(my_array)
