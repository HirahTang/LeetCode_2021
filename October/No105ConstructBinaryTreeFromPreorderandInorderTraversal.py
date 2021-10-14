#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:25:27 2021

@author: hirahtang
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def defineTree(preorder, inorder):
        if preorder != [] and inorder != []:
            r_val = preorder.pop(0)
            root = TreeNode(r_val)
            
            root.left = Solution.defineTree(preorder, inorder[:inorder.index(r_val)])
            root.right = Solution.defineTree(preorder, inorder[inorder.index(r_val)+1:])
            
            return root
        else:
            return 
    
    def buildTree(self, preorder, inorder):
        if preorder == inorder == []:
            return -1
        else:
            
            return Solution.defineTree(preorder, inorder)
        
        
# =============================================================================
# Optimised Solution
# =============================================================================
class Solution:

    def buildTree(self, preorder, inorder):
        pos = {v:i for i,v in enumerate(inorder)}
        preorder = preorder[::-1]
        def rec(left, right):
            if left <= right and len(preorder):
                root_val = preorder.pop()
                node = TreeNode(root_val)
                node.left = rec(left, pos[root_val] - 1)
                node.right = rec(pos[root_val] + 1, right)
                return node
        return rec(0, len(preorder) - 1)