#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 17:11:42 2021

@author: hirahtang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head
#        ite = 0
        while True:
            slow = slow.next
            if not fast.next or not fast.next.next:
                return False
            fast = fast.next.next
#            ite += 1
#            if not fast:
#                return False
            if slow == fast:
                return True
            