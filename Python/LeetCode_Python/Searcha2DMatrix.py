#!/usr/bin/env python
# coding=utf-8
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix[0]) < 1:
            return False
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            if matrix[i][0] <= target <= matrix[i][-1]:
                start, end = 0, column - 1
                while start <= end:
                    middle = (start + end) // 2
                    #print(middle)
                    if matrix[i][middle] == target:
                        return True
                    elif matrix[i][middle] < target:
                        start = middle + 1
                    elif matrix[i][middle] > target:
                        end = middle - 1
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while high >= low:

            mid = (high + low) // 2
            value = matrix[mid // cols][mid % cols]     # convert mid to a row and column

            if target == value:
                return True
            if target > value:
                low = mid + 1
            else:
                high = mid - 1

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)

        for i in range(row):
            if target in matrix[i]:
                return True
        return False
