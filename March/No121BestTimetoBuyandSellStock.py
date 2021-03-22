#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:25:22 2021

@author: hirahtang
"""

# =============================================================================
# 121. Best Time to Buy and Sell Stock
# =============================================================================

# class Solution:
    
#     def doublepointers(prices, max_g, min_g, max_c, min_c):
#         print (prices, max_g, min_g, max_c, min_c)
#         if min_g >= max_c:
#             if prices[min_g] >= prices[max_g]:
#                 return 0
#             else:
#                 return prices[max_g] - prices[min_g]
#         else:
#             max_c -= 1
#             if prices[max_c] > prices[max_g] and max_c > min_g:
#                 max_g = max_c
#             min_c += 1
#             if prices[min_c] < prices[min_g] and min_c < max_g:
#                 min_g = min_c
#             return Solution.doublepointers(prices, max_g, min_g, max_c, min_c)
    
#     def maxProfit(self, prices):
#         max_g = len(prices) - 1
#         min_g = 0
#         max_c = len(prices) - 1
#         min_c = 0
#         return Solution.doublepointers(prices, max_g, min_g, max_c, min_c)
                
        
class Solution:

    def maxProfit(self, prices):
        minprice = max(prices)
        maxprofit = 0
        
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit

