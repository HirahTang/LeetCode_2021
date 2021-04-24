#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 23:52:37 2021

@author: TH
"""
# =============================================================================
# 101. Symmetric Tree
# =============================================================================
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def isSymmetric(self, root):
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)
        
        