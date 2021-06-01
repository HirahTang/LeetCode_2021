#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:42:54 2021

@author: hirahtang
"""

def b_search(nums, lower, upper):
    
    if lower >= (upper - 1) and nums[lower] > nums[upper]:
        return nums[upper]
    
    mid = (upper + lower) // 2
    # print (lower, upper, mid)
    if nums[mid] >= nums[lower]: # mid at the First Half
        
        lower = mid
        return b_search(nums, lower, upper)
    if nums[mid] <= nums[upper]: # mid at the Second Half
        upper = mid
        return b_search(nums, lower, upper)


def twitedlist(nums):
    lower = 0
    upper = len(nums) - 1
    
    return b_search(nums, lower, upper)
    
    