#!/usr/bin/env python
# coding=utf-8


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]
        :type: void
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()
        return
