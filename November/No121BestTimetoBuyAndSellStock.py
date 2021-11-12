#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:52:23 2021

@author: hirahtang
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = max(prices)
        maxprofit = 0
        
        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            maxprofit = max(maxprofit, prices[i] - minprice)
            
        return maxprofit