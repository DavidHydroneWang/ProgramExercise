#!/usr/bin/env python
# coding=utf-8


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[] for i in range(9)]
        columns = [[] for i in range(9)]
        blocks = [[] for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    pass
                else:
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])
                    blocks[i // 3 * 3 + j // 3].append(board[i][j])
        for B2L in rows, columns, blocks:
            for subList in B2L:
                if not len(subList) == len(set(subList)):
                    return False
        return True
