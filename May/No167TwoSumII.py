#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 16:34:18 2021

@author: hirahtang
"""

# =============================================================================
# 167. Two Sum II - Input array is sorted
# =============================================================================

class Solution:
    def binarysearch(target, num, upper, lower):
        # print (upper, lower)
        mid = (upper + lower) // 2
        if upper - lower == 1 and target != num[upper] and target != num[lower]:
            # print ('Not Found')
            return -1
        if target == num[upper]:
            # print ('upper:', upper)
            return upper
        if target == num[lower]:
            # print ('lower:', lower)
            return lower
        
        
        
        
        if target > num[mid]:
            lower = mid
            return Solution.binarysearch(target, num, upper, lower)
        elif target < num[mid]:
            upper = mid
            return Solution.binarysearch(target, num, upper, lower)
        else:
            # print ('mid:', mid)
            return mid
            
    
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            find = Solution.binarysearch(target - numbers[i], numbers, len(numbers) - 1, i+1)
            # print (find)
            if find != -1:
                # print (find)
                return [i+1, find+1]
            else:
                continue
            
                
        

