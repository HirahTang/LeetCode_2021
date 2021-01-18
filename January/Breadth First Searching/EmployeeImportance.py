#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:27:08 2021

@author: hirahtang
"""

# =============================================================================
# No. 690 Employee Importance
# =============================================================================

class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    
    def bfs(employees, queue, value):
        if queue == []:
            return value
        current_staff = queue[0]
        del queue[0]
        for staff in employees:
            if current_staff == staff.id:
                value += staff.importance
                if staff.subordinates != []:
                    for i in staff.subordinates:
                        queue.append(i)
        return Solution.bfs(employees, queue, value)
                
    
    def getImportance(self, employees, id: int) -> int:
        value = 0
        for staff in employees:
            if staff.id == id:
                value += staff.importance
                queue = staff.subordinates
        return Solution.bfs(employees, queue, value)