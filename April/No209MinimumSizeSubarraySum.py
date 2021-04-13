#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:14:10 2021

@author: hirahtang
"""

class Solution:
    
# =============================================================================
#     O(n) Approach: Sliding Window
# =============================================================================
    
    def minSubArrayLen(self, target, nums):
        
        if sum(nums) < target:
            return 0
        elif sum(nums) == target:
            return len(nums)
        
        output = len(nums)+1
        pointer = 0
        
        continuous_l = []
        
        while pointer <= len(nums):
            # print (pointer, continuous_l)
            if sum(continuous_l) < target:
                if pointer  == len(nums):
                    break
                else:
                    continuous_l.append(nums[pointer])
                    pointer += 1

            elif sum(continuous_l) >= target:
                # output.append(len(continuous_l))
                output = min(output, len(continuous_l))
                continuous_l.pop(0)

        if output == len(nums) + 1:
            return 0
        else:
            return output
        
# =============================================================================
#     O(nlog(n)) Approach: Binary Search
# =============================================================================
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        sums = [n for n in nums]
        
        #sums[i]=sums[i−1]+nums[i]
				#sums[0] = nums[0]+nums[1]
        for i in range(len(sums) - 1):
            sums[i + 1] += sums[i]
        
        for i in range(len(sums)):
            right = self.helper(i, len(sums), target+sums[i]-nums[i], sums)
            if right < len(sums):
                res = min(res, right - i + 1)
                
        return res if res!= float('inf') else 0
        
        
    def helper(self, left, right, key, sums):
        while left < right:
            mid = (int)(left + (right-left)/2)
            if sums[mid] >= key:
                right = mid 
            else:
                left = mid + 1
        return left