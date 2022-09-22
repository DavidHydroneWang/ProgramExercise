#!/usr/bin/env python
# coding=utf-8
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [ i[0] for i in matrix]
        row = len(matrix)
        column = len(matrix[0])
        res = []
        res += matrix[0]
        for i in range(1, row - 1):
            res.append(matrix[i][column - 1])
        res += matrix[row - 1][::-1]
        for i in range(row - 2, 0, -1):
            res.append(matrix[i][0])
        lefted = []
        for i in range(1, row - 1):
            if matrix[i][1: column - 1]:
                lefted.append(matrix[i][1: column - 1])


        return res + self.spiralOrder(lefted)


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        ans = []
        while True:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):
                ans.append(matrix[down][i])
            down -= 1
            if down < up:
                break
            for i in range(down, up - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ans


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        seen = set()
        def dfs(i, j, d):
            seen.add((i, j))
            res.append(matrix[i][j])
            if d == 'r':
                if j + 1 < n and (i, j + 1) not in seen:
                    dfs(i, j + 1, d)
                elif i + 1 < m and (i + 1, j) not in seen:
                    dfs(i + 1, j , 'd')
            elif d == 'd':
                if i + 1 < m and (i + 1, j) not in seen:
                    dfs(i + 1, j , d)
                elif j and (i, j - 1) not in seen:
                    dfs(i, j - 1, 'l')
            elif d == 'l':
                if j and (i, j - 1) not in seen:
                    dfs(i, j - 1, d)
                elif i and (i - 1, j) not in seen:
                    dfs(i - 1, j, 'u')
            else:
                if i and (i - 1, j) not in seen:
                    dfs(i - 1, j, d)
                elif j + 1 < n and (i, j + 1) not in seen:
                    dfs(i, j + 1, 'r')
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        dfs(0, 0, 'r')
        return res


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        spiral = []
        row, col = 0, -1
        d_row, d_col = 0, 1     # movement direction
        row_leg, col_leg = len(matrix[0]), len(matrix)-1    # steps before change of direction
        leg_count = 0                                       # count of steps in current direction

        for _ in range(len(matrix[0]) * len(matrix)):

            row += d_row
            col += d_col
            spiral.append(matrix[row][col])
            leg_count += 1

            # change direction
            if (d_col != 0 and leg_count == row_leg) or (d_row != 0 and leg_count == col_leg):
                if d_col != 0:
                    row_leg -= 1
                else:
                    col_leg -= 1
                d_row, d_col = d_col, -d_row
                leg_count = 0

        return spiral
