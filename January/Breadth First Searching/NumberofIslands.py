#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:29:10 2021

@author: TH
"""
class Solution:
    def numIslands(self, grid): # My Approach but fail to pass the submission time limit
        # for i in grid:
        #     for j in i:
        #         print (j)
        
# =============================================================================
#         We formed a m by n grid in this step
#         
#         11 12 13 ... 1m
#         21 22 23 ... 2m
#         31 32 33 ... 3m
#         .  ......    .
#         .            .
#         .  ......    .
#         (n-1)1 (n-1)2 (n-1)m
#         n1 n2 n3 ... nm         
# =============================================================================
        
        m = len(grid[0]) # The width of grid
        n = len(grid) # The length of grid
        # print (m, n)
        
        lands = [] # A list to store all the "1"'s positions
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    lands.append((i,j))
        # lands = set(lands)
        # print (lands)
        # for i in lands:
        #     print (grid[i[0]] [i[1]])
        if len(lands) == 0: return 0   # return 0 if only sea
        
        # visited = []
        
        
        queue = []
        num_islands = 0
        
        while len(lands) > 0:
            queue.append(lands[0])
            grid[lands[0][0]][lands[0][1]] = '0'
            # visited.append(list(lands)[0])
        
        
            while len(queue) > 0:
                # print ('current queue:', queue)
                # print ('left lands:', lands)
                # print ('visisted:', visited)
                size = len(queue)
                for i in range(size):
                    # print ('Checking lands:', queue[i])
                    if queue[i] in lands:
                        # print ("True")
                        goEast = (queue[i][0], queue[i][1] + 1)
                        if (queue[i][1] + 1) < m:
                            if grid[goEast[0]][goEast[1]] == '1':
                                queue.append(goEast)
                                grid[goEast[0]][goEast[1]] = '0'
                        
                        goSouth = (queue[i][0] + 1, queue[i][1])
                        if (queue[i][0] + 1) < n:
                            if grid[goSouth[0]][goSouth[1]] == '1':
                                queue.append(goSouth)
                                grid[goSouth[0]][goSouth[1]] = '0'
                        
                        goNorth = (queue[i][0] - 1, queue[i][1])
                        if (queue[i][0] - 1) >= 0:
                            if grid[goNorth[0]][goNorth[1]] == '1': 
                                queue.append(goNorth)
                                grid[goNorth[0]][goNorth[1]] = '0'
                            
                        goWest = (queue[i][0], queue[i][1] - 1)
                        if (queue[i][1] - 1) >= 0:
                            if grid[goWest[0]][goWest[1]] == '1':
                                queue.append(goWest)
                                grid[goWest[0]][goWest[1]] == '0'
                        
                    # queue.append(goEast)
                    # queue.append(goSouth)
                        lands.remove(queue[i])
                    # visited.append(i)
                for i in range(size):
                    queue.pop(0)
            # print ("An Island")
            num_islands += 1
        return num_islands