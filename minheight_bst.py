#!/usr/bin/python2

# Given a sorted (increasing order) array, write an 
# algorithm to create a binary tree with minimal height

import sys
import os

sys.path.append(os.getenv("HOME") + "/Code/Python/libst/")
from bst import BST

def minheight_bst(bst, array):
    
    if len(array) > 2:
        mid = len(array) / 2
        bst.insert(array[mid]) 
        minheight_bst(bst, array[:mid])
        minheight_bst(bst, array[mid+1:])
    elif len(array) > 0 and len(array) <= 2:
        for e in array:
            bst.insert(e)
    else:
        return


if __name__ == "__main__":
    
    array = range(1,99)
    bst = BST()
     
    minheight_bst(bst, array)    
    bst.print_tree("POSTORDER")
    if bst.is_balanced():
        print "balanced"
    else:
        print "not balanced"
    
