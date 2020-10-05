# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 06:08:53 2020

@author: CeLiang
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] =='1': 
                    layer =deque()
                    layer.append([i,j])
                    ans = ans+ 1
                    while layer:
                        for _ in range(len(layer)):
                            x,y = layer.popleft()
                            grid[x][y] ='0'
                            for new_x,new_y in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[i]) and grid[new_x][new_y] == '1':
                                    layer.append([new_x,new_y]) 
                                    grid[new_x][new_y] = '0'
                    
        return ans