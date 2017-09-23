# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 20:08:12 2017

@author: Derling
"""

class Node():
    # 1. Helper class for debugging
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def remove(self, value, parent):
        if value < self.value:
            if self.left: # if left child, may be in lower level
                return self.left.remove(value, self)
            else:
                return False
        elif value > self.value:
            if self.right: # if right child, may be in lower level
                return self.right.remove(value, self)
            else:
                return False # no right node, value not in lower level
        else: # we found the node with the value!
            ''' the node has both children, in which case we want to set the
                current value of the node to the next largest number, then 
                we want to remove that node with the value we just set it to'''
            if self.left and self.right:
                self.value = self.right.get_min() 
                self.right.remove(self.value, self)
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.left if self.left else self.right
            return True

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    def get_min(self):
        if not self.left:
            return self.value
        else:
            return self.left.get_min()

class BinarySearchTree():
    # 1. Implement a BST with insert and delete functions
    def __init__(self, root = None):
        self. root = root

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current):
        if current.value > value:
            if current.left:
                self._insert(value, current.left)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert(value, current.right)
            else:
                current.right = Node(value)

    def delete(self, value):
        if not self.root:
            return None
        else:
            if self.root.value == value: # root has the value
                ''' dummy node method - root value gets changed and other node
                    with that value will get removed from tree then set root to
                    dummys left which is the new origin'''
                dummy = Node(0)
                dummy.left = self.root
                result = self.root.remove(value, dummy)
                self.root = dummy.left
                return result
            else:
                return self.root.remove(value, None)

    def get_min(self):
        if self.root:# if tree not empty get minimmum value in tree
            return self.root.get_min()

    def get_max(self):
        if self.root: # if tree not empty get maximum value in tree
            return self.root.get_max()

if __name__ == '__main__':
    pass