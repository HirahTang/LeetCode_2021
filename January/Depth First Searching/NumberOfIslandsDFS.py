#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:33:01 2021

@author: hirahtang
"""

class Solution:
    def DFS(grid, dfs_l, m, n):
        
        if not dfs_l:
            return grid

        
        
         # DFS list
        # print (dfs_l)
        land = dfs_l.pop()
        
        if grid[land[0]][land[1]] == "1":
            grid[land[0]][land[1]] = "0"
            if land[0] < (m - 1):
                if grid[land[0] + 1][land[1]] == "1":
                    dfs_l.append((land[0] + 1, land[1]))
            if land[0] > 0:
                if grid[land[0] - 1][land[1]] == "1":
                    dfs_l.append((land[0] - 1, land[1]))
            if land[1] < (n - 1):
                if grid[land[0]][land[1] + 1] == "1":
                    dfs_l.append((land[0], land[1] + 1))
            if land[1] > 0:
                if grid[land[0]][land[1] - 1] == "1":
                    dfs_l.append((land[0], land[1] - 1))
            if not dfs_l:
                return grid
            return Solution.DFS(grid, dfs_l, m, n)
        else:
            return Solution.DFS(grid, dfs_l, m, n)
            
        
    
    
    def numIslands(self, grid):
        
        num = 0
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # print (i, j)
                    num += 1
                    grid = Solution.DFS(grid, [(i, j)], m, n)
        return num
        