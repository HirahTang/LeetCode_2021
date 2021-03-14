#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:59:30 2021

@author: hirahtang
"""

# =============================================================================
# 542. 01 Matrix
# =============================================================================

# from collections import deque

class Solution:
    def BFS(matrix, queue, distance):
        # print (queue)

        adjacent = []
        for current_p in queue:
            # print (current_p)
            if current_p[0] > 0: # Current point is not at the top
                adjacent.append((current_p[0] - 1, current_p[1])) # Look at the point above it
            if current_p[0] < len(matrix) - 1: # Current point is not at the bottom
                adjacent.append((current_p[0] + 1, current_p[1])) # Look at the point beneath it
            if current_p[1] > 0: # Current point is not at the leftmost
                adjacent.append((current_p[0], current_p[1] - 1)) # Look at the point left to it
            if current_p[1] < len(matrix[0]) - 1:
                adjacent.append((current_p[0], current_p[1] + 1)) # Look at the point left to it
        # print (adjacent)
        for i in adjacent:
            # print (i[0], i[1])
            if matrix[i[0]][i[1]] == 0:
                
                return distance
        for i in range(len(queue)):
            queue.pop(0)
        for i in adjacent:
            queue.append(i)
        distance += 1
        return Solution.BFS(matrix, queue, distance)
    def updateMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    queue = [(i, j)]
                    matrix[i][j] = Solution.BFS(matrix, queue, matrix[i][j])
        return matrix
        