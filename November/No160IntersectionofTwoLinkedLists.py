#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 14:21:39 2021

@author: hirahtang
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a