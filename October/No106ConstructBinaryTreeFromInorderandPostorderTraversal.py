#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:59:29 2021

@author: hirahtang
"""

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def buildTreerec(inorder, postorder):
        if len(inorder) == 1:
            root = TreeNode(inorder[0])
            return root
        
        for i in postorder[::-1]:
            if i in inorder:
                root_v = i
                break
        
        root = TreeNode(root_v)
        pivot_inorder = inorder.index(root_v)
        pivot_postorder = postorder.index(root_v)
        if inorder[pivot_inorder+1:] != []:
            root.right = Solution.buildTreerec(inorder[pivot_inorder+1:], postorder[:pivot_postorder])
        if inorder[:pivot_inorder] != []:
            root.left = Solution.buildTreerec(inorder[:pivot_inorder], postorder[:pivot_postorder])
        return root

    
    def buildTree(self, inorder, postorder):
        
        return Solution.buildTreerec(inorder, postorder)