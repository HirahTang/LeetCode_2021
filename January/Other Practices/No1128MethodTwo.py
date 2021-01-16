#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:56:20 2021

@author: hirahtang
"""

# =============================================================================
# # 1128. Number of Equivalent Domino Pairs
# =============================================================================

import itertools

class Solution:
	def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
		ht = {}
		for dom in dominoes:
			ht[tuple(sorted(dom))] = ht.get(tuple(sorted(dom)),0) + 1
		count = 0
		for pair in ht:
			count += ht[pair]*(ht[pair]-1)//2
		return count

class Solution1:
	def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
		if len(dominoes) <= 1:
			return 0

		combs = [x for x in itertools.combinations(dominoes,2)]
		count = 0
		for item in combs:
			if min(item[0]) == min(item[1]) and max(item[0]) == max(item[1]):
				count += 1
		return count