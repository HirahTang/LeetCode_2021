#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:39:01 2021

@author: hirahtang
"""
# =============================================================================
# 134. Gas Station
# =============================================================================

class Solution:

# =============================================================================
# Brute Force    
# =============================================================================

    def check(start, gas, cost):
        
        gas = gas[start:] + gas[:start]
        cost = cost[start:] + cost[:start]
        
        tank = 0
        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]
            if tank < 0:
                return False
        return True
    
    def canCompleteCircuit(self, gas, cost):
        for start in range(len(gas)):
            if Solution.check(start, gas, cost):
                return start
        return -1
        
    
# =============================================================================
# Greedy
# =============================================================================

    def canCompleteCircuit(self, gas, cost):
	    trip_tank, curr_tank, start, n = 0, 0, 0, len(gas)
	    for i in range(n):
		    trip_tank += gas[i] - cost[i]
		    curr_tank += gas[i] - cost[i]
		    if curr_tank < 0:
			    start = i + 1
			    curr_tank = 0 
	    return start if trip_tank >= 0 else -1