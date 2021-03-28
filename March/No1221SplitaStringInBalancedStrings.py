#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:32:48 2021

@author: hirahtang
"""
# from collections import Counter

# =============================================================================
# 1221. Split a String in Balanced Strings
# =============================================================================

class Solution:
    def balancedStringSplit(self, s):
        pairs = 0
        # j = 0
        check = {'R':0, 'L':0}
        for i in range(2, len(s)+2, 2):
            # check = Counter(s[j:i])
            check[s[i-2]] += 1
            check[s[i-1]] += 1
            if check['L'] == check['R']:
                # print (j, i, s[j:i], check)
                pairs += 1
                # j = i
                check['L'] = 0
                check['R'] = 0
                
            else:
                continue
            
        return pairs
        