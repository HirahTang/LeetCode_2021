#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:01:34 2021

@author: hirahtang
"""

# =============================================================================
# 122. Best Time to Buy and Sell Stock II
# =============================================================================

class Solution:
    def maxProfit(self, prices):
        profit = 0
        buyin = False
        stock_p = 0
        
# =============================================================================
#         we have four cases, considering the states of whether holding a stock, 
#         and whether the stock is going to drop or rise in the next transacting day
# =============================================================================
        
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i] and buyin == False:
                buyin = True
                stock_p = prices[i]
                # print (stock_p)
            if prices[i + 1] < prices[i] and buyin == False:
                continue
            if prices[i + 1] > prices[i] and buyin == True:
                continue
            if prices[i + 1] < prices[i] and buyin == True:
                profit += (prices[i] - stock_p)
                # print (profit)
                buyin = False
                stock_p = 0
        if buyin == True:
            profit += (prices[-1] - stock_p)
        return profit
                
        