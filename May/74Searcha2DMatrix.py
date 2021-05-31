#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 13:21:52 2021

@author: hirahtang
"""

# =============================================================================
# 74. Search a 2D Matrix
# =============================================================================

class Solution:
    
    def binarysearch(target, nums, lower, upper):
        
        if nums[lower] == target:
            return lower
        if nums[upper] <= target:
            return upper
        
        if lower >= (upper - 1):
            return lower
        else:
            mid = (lower + upper) // 2

            if nums[mid] >= target:
                upper = mid
                return Solution.binarysearch(target, nums, lower, upper)
            elif nums[mid] <= target:
                lower = mid
                return Solution.binarysearch(target, nums, lower, upper)
    
    def searchMatrix(self, matrix, target):
        rows = [row[0] for row in matrix]
        row_n = Solution.binarysearch(target, rows, 0, len(rows) - 1)
        col_n = Solution.binarysearch(target, matrix[row_n], 0, len(matrix[0]) - 1)
        return matrix[row_n][col_n] == target