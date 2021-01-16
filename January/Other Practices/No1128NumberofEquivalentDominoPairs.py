#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:01:45 2021

@author: hirahtang
"""

# =============================================================================
# 1128. Number of Equivalent Domino Pairs
# =============================================================================

from collections import Counter

class Solution:
    
    def swap(domi):
        return domi[1] + domi[0]
        # return (domi[0] == domj[0] and domi[1] == domj[1]) or (domi[0] == domj[1] and domi[1] == domj[0])
    
    
    
    def numEquivDominoPairs(self, dominoes):
        
        pairs = 0
        dominoes = [''.join(list(map(str, i))) for i in dominoes]
        check_domi = Counter(dominoes)

        print (check_domi)
        for i in range(len(dominoes)):
            check_domi[dominoes[i]] -= 1
            # if check_domi[i] >= 1:
            pairs += check_domi[dominoes[i]]
            
            if Solution.swap(dominoes[i]) in check_domi and dominoes[i] != Solution.swap(dominoes[i]):
                pairs += check_domi[Solution.swap(dominoes[i])]
        #     for j in range(i+1, len(dominoes)):
        #         if Solution.equivalent(dominoes[i], dominoes[j]):
        #             pairs += 1
            
        return pairs
        
        