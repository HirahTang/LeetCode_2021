#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:34:33 2021

@author: hirahtang
"""

# =============================================================================
# 112. Path Sum
# =============================================================================


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, sum_):
        if root==None:
            return False
        #check if leaf node and target sum achieved
        if sum_ == root.val and root.left == None and root.right == None:
            return True
        return self.hasPathSum(root.left, sum_ - root.val) or self.hasPathSum(root.right, sum_ - root.val)
    
    # def hasPathSum(self, root, sum_):
    #     def stackPathsum(root, sum_, stack):
            
    #         if root == None:
                
    #             return False
            
    #         node_stack = [root]
    #         sum_stack = [sum_ - root.val]
            
            
    #         while node_stack != []:
                
    #             current_node = node_stack.pop()
    #             current_sum = sum_stack.pop()
                
    #             if current_node.left == None and current_node.right == None and current_sum == sum_:
    #                 return True
                
    #             if current_node.left != None:
    #                 node_stack.append(current_node.left)
    #                 sum_stack.append(current_sum - current_node.left.val)
    #             if current_node.left != None:
    #                 node_stack.append(current_node.left)
    #                 sum_stack.append(current_sum - current_node.left.val)
    #         return False
            
            # if root.left == None and root.right == None:
            #     if sum(stack) == sum_:
            #         return True
            #     else:
                    
            
            # elif :
            #     Solution.stackPathsum(root.left, sum_, )
                