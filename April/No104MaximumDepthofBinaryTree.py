#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:45:27 2021

@author: hirahtang
"""


# =============================================================================
# 104. Maximum Depth of Binary Tree
# =============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(queue, layer):
        new_queue = []
        for i in queue:
            if i.left:
                new_queue.append(i.left)
            if i.right:
                new_queue.append(i.right)
        if len(new_queue) > 0:
            layer += 1
            return Solution.dfs(new_queue, layer)
        else:
            return layer
    
    def maxDepth(self, root):
        
        if not root:
            return 0
        
        queue = [root]
        layer = 1
        
        return Solution.dfs(queue, layer)
        
    
# =============================================================================
#     A Simpler Approach
# =============================================================================
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))