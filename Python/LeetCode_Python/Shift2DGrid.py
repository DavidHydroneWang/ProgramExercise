#!/usr/bin/env python
# coding=utf-8
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        def shift(grid):
            m = len(grid)
            n = len(grid[0])
            temp = grid[m - 1][n - 1]
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if j == 0 and i == 0:
                        grid[i][j] = temp
                    elif j == 0:
                        grid[i][j] = grid[i - 1][n - 1]
                    else:
                        grid[i][j] = grid[i][j - 1]

        for i in range(k):
            shift(grid)

        return grid


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * n for _ in range(m)]

        k %= m * n

        for i in range(m):
            for j in range(n):
                index = (i * n + j + k) % (m * n)
                x = index // n
                y = index % n
                ans[x][y] = grid[i][j]

        return ans


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        n = rows * cols

        result = [[]]
        for i in range(n):                  # iterate over all indices of grid
            if len(result[-1]) == cols:     # make a new empty row
                result.append([])
            prev = (i - k) % n              # index of element to move here
            r, c = divmod(prev, cols)       # convert index in n to row and col
            result[-1].append(grid[r][c])

        return result



class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # m * n temp array
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        m = len(grid)
        n = len(grid[0])
        # Compute final location
        true_k = k % (m * n)
        # row move
        move_i = true_k // n
        # col move
        move_j = true_k % n

        for i in range(m):
            for j in range(n):
                new_i = i + move_i
                # move one row if move_j + j >= n
                if move_j + j >= n:
                    new_i += 1
                new_i %= m
                new_j = (j + move_j) % n
                new_grid[new_i][new_j] = grid[i][j]
        return new_grid
