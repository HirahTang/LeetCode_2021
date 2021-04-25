#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:48:21 2021

@author: TH
"""
# =============================================================================
# 16. 3Sum Closest
# =============================================================================

class Solution:
    
    # def find_closest(nums, target, lower):
        
        
    #     upper = len(nums) - 1
        
    #     while (upper - lower) > 1:
    #         mid = (upper - lower) // 2 + lower
    #         # print ("mid: ",nums[mid])
    #         if nums[mid] <= target:
    #             # print("Lower Up: Lower: {}, Upper: {}".format(lower, upper))
    #             lower = mid
    #         else:
    #             # print("Upper Down: Lower: {}, Upper: {}".format(lower, upper))
    #             upper = mid
    #     if nums[lower] < nums[upper]:
    #         return lower
    #     else:
    #         return upper
    
    # def threeSumClosest(self, nums, target):
    #     nums = sorted(nums)
    #     output = 0
    #     res = float('inf')
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             n_target = target - (nums[i] + nums[j])
    #             third = Solution.find_closest(nums, n_target, j+1)
    #             if abs(n_target - nums[third]) < res:
    #                 res = abs(n_target - third)
    #                 output = nums[i] + nums[j] + nums[third]
    #                 print (i, j, third)
    #     return output     
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        # O(n^2*log(n)) Approach
        
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        # O(n^2) Approach
        
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff