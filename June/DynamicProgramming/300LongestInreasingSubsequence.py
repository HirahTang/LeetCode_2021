#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:11:32 2021

@author: hirahtang
"""

# =============================================================================
# 300. Longest Increasing Subsequence 
# =============================================================================
# Dynamic Programming
class Solution:
    def lengthOfLIS_1(self, nums):
        
        dp = [1 for content in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    # Dynamic Programming + Greedy (Recursive Binary Search)
    def lengthofLIS_2(self, nums):
        
        def find_index(value, arr_, lower, upper):
            if lower >= upper:
                # if value <= arr_[lower]:
                #     return lower
                # print (lower, arr_[lower])
                return lower
            
            mid = (lower + upper)  >> 1
            if arr_[mid] >= value:
                upper = mid
                # print (upper)
                return find_index(value, arr_, lower, upper)
            else:
                lower = mid + 1
                # print (lower)
                return find_index(value, arr_, lower, upper)
            
        
        tail = [nums[0]]
        for i in nums[1:]:
            if i > tail[-1]:
                tail.append(i)
                # print (tail, i)
            # elif i <= tail[0]:
            #     continue
            else:
                tail[find_index(i, tail, 0, len(tail) - 1)] = i
                # print (tail)
                
        return len(tail)