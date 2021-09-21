#!/usr/bin/env python
# coding=utf-8


def quick_sort(start_index, end_index, array=[]):
    quick_sort_stack = []
    root_param = {"startIndex": start_index, "endIndex": end_index}
    quick_sort_stack.append(root_param)
    while len(quick_sort_stack) > 0:
        param = quick_sort_stack.pop()
#        print(param)
        pivot_index = partition(param.get("startIndex"),
                                param.get("endIndex"), array)
#        print(pivot_index)
        if param.get("startIndex") < pivot_index - 1:
            left_param = {"startIndex": param.get("startIndex"),
                          "endIndex": pivot_index - 1}
#            print(left_param)
            quick_sort_stack.append(left_param)
        if pivot_index + 1 < param.get("endIndex"):
            right_param = {"startIndex": pivot_index + 1,
                           "endIndex": param.get("endIndex")}
#            print(right_param)
            quick_sort_stack.append(right_param)


def partition(start_index, end_index, array=[]):
#    print(start_index)
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


my_list = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
quick_sort(0, len(my_list)-1, my_list)
print(my_list)
