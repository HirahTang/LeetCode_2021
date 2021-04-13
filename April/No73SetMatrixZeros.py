#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:57:24 2021

@author: hirahtang
"""

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = {'col':set([]),
                 'row':set([])}
        
        for col in range(len(matrix)):
            for row in range(len(matrix[col])):
                if matrix[col][row] == 0:
                    zeros['col'].add(col)
                    zeros['row'].add(row)
        
        for col in range(len(matrix)):
            for row in range(len(matrix[col])):
                if col in zeros['col'] or row in zeros['row']:
                    matrix[col][row] = 0
        return matrix
        