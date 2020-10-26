# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:24:05 2020

@author: CeLiang
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for j in range(1,m):
            grid[j][0] = grid[j-1][0] + grid[j][0]

        for i in range(1,n):
            for j in range(1,m):
                grid[j][i] = grid[j][i] + min(grid[j-1][i],grid[j][i-1])

        return grid[-1][-1]