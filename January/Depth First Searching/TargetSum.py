#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:06:49 2021

@author: hirahtang
"""


# =============================================================================
# No.494 Target Sum
# =============================================================================

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """


        # then i found some intermediate results can be cached...

        # DP, by cache the intermediate results
        def dfs(depth, sum_all=0, num_ways_cache={}):
            if depth >= len(nums):  # now we are in the bottom level
                # print depth, sum_all
                if sum_all == S:
                    return 1
                return 0
            if (depth, sum_all) in num_ways_cache:
                return num_ways_cache[(depth, sum_all)]
            num_of_ways = dfs(depth + 1, sum_all - nums[depth], num_ways_cache) + \
                          dfs(depth + 1, sum_all + nums[depth], num_ways_cache)
            num_ways_cache[(depth, sum_all)] = num_of_ways
            return num_of_ways
        return dfs(0)