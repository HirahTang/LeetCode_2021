#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:21:30 2021

@author: hirahtang
"""

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
    

    def get(self, index: int) -> int:
        
        if index > self.size-1:
            # print (index, self.size)
            return -1
        
        node = self.head
        while index > 0:
            node = node.next
            index -= 1
        return node.val

    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
            self.size += 1
            return
        self.head = Node(val, self.head)
        self.size += 1
#        print ("Addhead", self.size)
        return

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
            self.size += 1
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)
        self.size += 1
        return 
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size:
            return
        
        if self.size == 0 or index == 0:
            self.addAtHead(val)
            return
        if index == (self.size):
            self.addAtTail(val)
            return
        node = self.head
        
        while index > 1:
            node = node.next
            index -= 1
        
        node.next = Node(val, node.next)
        self.size += 1
#        print (self.size)
        return

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size - 1:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        if index == (self.size - 1):
            node = self.head
            while index > 1:
                node = node.next
                index -= 1
            node.next = None
            self.size -= 1
            return
        node = self.head
        while index > 1:
            node = node.next
            index -= 1
        node.next = node.next.next
        self.size -= 1
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)