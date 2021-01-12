#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:23:57 2021

@author: hirahtang
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    
    def recClone(visited, node):
        
        # 1. The current Node is empty
        
        if node is None:
            return None
        
        # 2. Current Node has zero neighbors
        
        if len(node.neighbors) == 0:
            return Node(val = node.val)
        
        # 3. Current Node is already visited, go to the node
        
        if node.val in visited:
            return visited[node.val]
        
        copy_Node = Node(val = node.val)
        
        visited[node.val] = copy_Node
        
        for i in node.neighbors:
            copy_Node.neighbors.append(Solution.recClone(visited, i))
        return copy_Node
            
        
        
        # if not stack:
        #     return visited
        # c_node = stack.pop()
        # if c_node not in visited:
        #     visited.add(c_node)
        #     for i in c_node.neighbors:
        #         stack.append(i)
        #         return Solution.recClone(visited, stack)
        # else:
        #     return Solution.recClone(visited, stack)
        
        
        
    def cloneGraph(self, Node):
        
        # output = []
        visited = {}
        # stack = []
        # output = []
        # node_dict = {}
        return Solution.recClone(visited, Node)

        
        