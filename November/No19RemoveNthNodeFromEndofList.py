#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:35:28 2021

@author: hirahtang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:
            return None
        
        if not head.next.next:
            if n == 1:
                head.next = None
                return head
            elif n == 2:
                head = head.next
                return head
        forward = head
        behind = head
        
        for i in range(n):
            forward = forward.next
            
#        if not forward.next:
#            if n > 1:
#                head = head.next
#                return head
        if not forward:
            head = head.next
            return head
        while forward.next:
            forward = forward.next
            behind = behind.next
        
        behind.next = behind.next.next
        return head