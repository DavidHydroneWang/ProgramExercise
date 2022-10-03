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

        r = 0
        c = len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            if target < matrix[r][c]:
                c -= 1
            else:
                r += 1

        return False


class Solution:


    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols-1

        while r < rows and c >= 0:

            if matrix[r][c] == target:
                return True

            if target > matrix[r][c]:
                r += 1
            else:
                c -= 1

        return False
