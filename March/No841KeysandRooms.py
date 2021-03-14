#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:58:39 2021

@author: hirahtang
"""

# =============================================================================
# 841. Keys and Rooms
# =============================================================================

class Solution:
    
    def DFS(rooms, opened, stack):
        if len(stack) == 0:
            return False
        keys = stack.pop()
        if len(rooms[keys]) > 0:
            for i in rooms[keys]:
                if i not in opened:
                    stack.append(i)
        opened.add(keys)
        if len(opened) == len(rooms):
            return True
#        elif len(stack) == 0:
#            return False
        else:
            return Solution.DFS(rooms, opened, stack)
    
    def canVisitAllRooms(self, rooms):
        if len(rooms) == 1:
            return True
        return Solution.DFS(rooms, set([0]), [i for i in rooms[0]])
        