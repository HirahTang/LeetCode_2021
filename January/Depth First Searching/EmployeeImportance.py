#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:32:53 2021

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
    
    def dfs(employees, stack, value):
        if stack == []:
            return value
        current_staff = stack.pop()
        for staff in employees:
            if current_staff == staff.id:
                value += staff.importance
                if staff.subordinates != []:
                    for i in staff.subordinates:
                        stack.append(i)
        return Solution.dfs(employees, stack, value)
                
    
    def getImportance(self, employees, id: int) -> int:
        value = 0
        for staff in employees:
            if staff.id == id:
                value += staff.importance
                stack = staff.subordinates
        return Solution.dfs(employees, stack, value)
                
        
                
        