#!/usr/bin/env python
# coding=utf-8


def find_median_sorted_arrays(array_A, array_B):
    m, n = len(array_A), len(array_B)
    if m > n:
        array_A, array_B, m, n = array_B, array_A, n, m

    if n == 0:
        raise ValueError
    start, end, half_len = 0, m, (m + n + 1) // 2
    while start <= end:
        i = (start + end) // 2
        j = half_len - i
        if i < m and array_B[j-1] > array_A[i]:
            start = i + 1
        elif i > 0 and array_A[i-1] > array_B[j]:
            end = i - 1
        else:
            if i == 0:
                max_of_left = array_B[j-1]
            elif j == 0:
                max_of_left = array_A[i-1]
            else:
                max_of_left = max(array_A[i-1], array_B[j-1])

            if (m+n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = array_B[j]
            elif j == n:
                min_of_right = array_A[j]
            else:
                min_of_right = min(array_A[i], array_B[j])
            return (max_of_left + min_of_right) / 2.0


my_array_A = list([3, 5, 6, 7, 8, 12, 20])
my_array_B = list([1, 10, 17, 18])
print(find_median_sorted_arrays(my_array_A, my_array_B))
