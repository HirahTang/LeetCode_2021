#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:47:35 2021

@author: hirahtang
"""

# =============================================================================
# 剑指 Offer 53 - II. 0～n-1中缺失的数字
# =============================================================================

class Solution:
    def missingNumber(self, nums):
        
        
        
        lower = 0
        upper = len(nums) - 1
        
        if nums[-1] == upper:
            return upper + 1
        if nums[0] != 0:
            return 0
        
        while lower < upper - 1:
            mid = (lower + upper) // 2
            if (upper - mid) < (nums[upper] - nums[mid]):
                lower = mid
            elif (mid - lower) < (nums[mid] - nums[lower]):
                upper = mid
            else:
                continue
        if upper != nums[upper]:
            return upper
        if lower != nums[lower]:
            return lower