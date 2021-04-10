#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:47:29 2021

@author: hirahtang
"""

# =============================================================================
# 867. Transpose Matrix
# =============================================================================

class Solution:
    def transpose(self, matrix):
        trans = [[] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                trans[j].append(matrix[i][j])
                
        return trans
    def transpose(self, A): # More efficient
        res = []
        for i in range(len(A[0])):
            temp = []
            for j in range(len(A)):
                temp.append(A[j][i])
            res.append(temp)
        return res
        