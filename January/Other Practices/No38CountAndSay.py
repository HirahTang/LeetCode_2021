#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:13:57 2021

@author: hirahtang
"""

# =============================================================================
# 38. Count and Say
# =============================================================================

# from collections import Counter

class Solution:
    def count(cur):
        # cur = Counter(cur)
        diff_p = []
        ret = ""
        for i in range(1, len(cur)):
            if cur[i] != cur[i-1]:
                diff_p.append(i)
                # print (i)
        start = 0
        for ends in diff_p:
            ret += str(ends - start) + cur[start]
            start = ends
        ends = len(cur)
        ret += str(ends - start) + cur[start]
        # print (ret)
        # print (diff_p)
        return ret
        
            
    
    def countAndSay(self, n):
        
        cur = "1"
        num = 1
        while num + 1 <= n:
            cur = Solution.count(cur)
            num += 1
        return cur
            
        