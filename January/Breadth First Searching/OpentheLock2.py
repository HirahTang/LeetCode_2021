#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:37:50 2021

@author: TH
"""
# =============================================================================
# LeetCode No.752 Open the Lock
# 
# Optimised Approaches(BFS) from the discuss board
# =============================================================================
class Solution:
    def openLock(self, deadends, target):
        # BFS sol
        deadends = set(deadends)
        if target in deadends or "0000" in deadends: # start/end in deadends ==> impossible
            return -1
        moves = {'0':['1','9'], '1':['0','2'], '2':['1','3'], '3':['2','4'], '4':['3','5'], \
                 '5':['4','6'], '6':['5','7'], '7':['6','8'], '8':['7','9'], '9':['8','0']}
        q = ["0000"]
        seen = deadends
        seen.add("0000")
        res = 0
        while q:
            nxt = []
            for s in q:
                if s == target:
                    return res
                l = list(s)
                for i in range(len(l)): # for each of the 4 digits
                    for n in moves[l[i]]: # turn the digit up or down
                        ss = "".join(l[:i]+[n]+l[i+1:]) # the result string after turning on digit
                        if ss not in seen:
                            nxt.append(ss)
                            seen.add(ss)
            q = nxt
            res += 1
            
        return -1