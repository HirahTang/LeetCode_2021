#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 12:09:40 2021

@author: hirahtang
"""
# =============================================================================
# 33. Search in Rotated Sorted Array
# =============================================================================
class Solution:
    
    def binarysearch(nums, target, lower, upper):
        
        if nums[lower] == target:
            return lower
        if nums[upper] == target:
            return upper
        
        if  upper <= (lower + 1):
            return -1
        
        mid = (upper + lower + 1) // 2
        
        if target >= nums[lower]: # Target in the first half
            if nums[mid] >= target:
                upper = mid
                
                # print (upper, lower)
                
                return Solution.binarysearch(nums, target, lower, upper)
            elif nums[lower] <= nums[mid] <= target:
                lower = mid
                
                # print (upper, lower)
                
                return Solution.binarysearch(nums, target, lower, upper)
            elif nums[mid] <= nums[upper]:
                upper = mid
                
                # print (upper, lower)
                
                return Solution.binarysearch(nums, target, lower, upper)
        elif target <= nums[upper]: # Target in the second half
            if nums[mid] >= nums[lower]:
                lower = mid
                
                # print (upper, lower)
                
                return Solution.binarysearch(nums, target, lower, upper)
            elif nums[mid] <= target <= nums[upper]:
                lower = mid
                
                # print (upper, lower)
                
                return Solution.binarysearch(nums, target, lower, upper)
            elif target <= nums[mid] <= nums[upper]:
                upper = mid
                
                # print (upper, lower)
                
                return Solution.binarysearch(nums, target, lower, upper)
    def search(self, nums, target):
        
        if nums[-1] < target < nums[0]:
            return -1
        
        lower = 0
        upper = len(nums) - 1
        # print (upper, lower)
        
        return Solution.binarysearch(nums, target, lower, upper)
        
                
            
        
        
        
