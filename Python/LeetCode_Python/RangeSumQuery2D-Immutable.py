#!/usr/bin/env python
# coding=utf-8
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.pre_sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for row in range(rows):
            for col in range(cols):
                self.pre_sum[row + 1][col + 1] = self.pre_sum[row + 1][col] + self.pre_sum[row][col + 1] - self.pre_sum[row][col] + matrix[row][col]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row2 + 1][col1] - self.pre_sum[row1][col2 + 1] + self.pre_sum[row1][col1]
