#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:57:57 2021

@author: hirahtang
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node'):
        def bfs(queue):
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
            queue_next = []
            for node in queue:
                if node.left:
                    queue_next.append(node.left)
                    queue_next.append(node.right)
                else:
                    return root
                    break
            return bfs(queue_next)
        
        if not root:
            return None
        return bfs([root])