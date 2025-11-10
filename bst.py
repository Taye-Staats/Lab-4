import math
import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**6)

BinTree: TypeAlias = Union["Node", None]

@dataclass(frozen=True)
class Node:
    value: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree

@dataclass(frozen=True) 
class Point2:
    x: float
    y: float

def distance_from_origin(self) -> float:
    return math.sqrt(self.x ** 2 + self.y ** 2)

# return if given bst is empty
def is_empty(bst: BinarySearchTree) -> bool:
    if bst.tree == None:
        return True
    else:
        return False

# insert given value into given bst
def insert(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    return BinarySearchTree(comes_before, insert_helper(bst.tree, value))

# helper function for insert function
def insert_helper(tree: BinTree, value: Any) -> BinTree:
    if tree != None: # insert in left or right depending on if given value is less/greater than current value in tree
        if comes_before(value, tree.value):
            return Node(tree.value, insert_helper(tree.left, value), tree.right)
        return Node(tree.value, tree.left, insert_helper(tree.right, value))
    else: # actually insert if current tree is None
        return Node(value, None, None)

# return if a is less than b
def comes_before(a: Any, b: Any) -> bool:
    return a < b

# return whether given value is in binary search tree
def lookup(bst: BinarySearchTree, value: Any) -> bool:
    return lookup_helper(bst.tree, value)

# helper function for lookup function
def lookup_helper(tree: BinTree, value: Any) -> bool:
    if tree == None or tree.value == None:
        return False
    elif tree.value == value:
        return True
    elif comes_before(value, tree.value):
        return lookup_helper(tree.left, value)
    else:
        return lookup_helper(tree.right, value)

# delete given value from given binary search tree
def delete(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    return BinarySearchTree(comes_before, delete_helper(bst.tree, value))

# helper function for delete function
def delete_helper(tree: BinTree, value: Any) -> BinTree:
    if tree == None:
        return tree
    else:
        root_value = tree.value
        l = tree.left
        r = tree.right
        
        if root_value == value:
            return delete_root(tree)
        elif root_value < value:
            return Node(root_value, l, delete_helper(r, value))
        else:
            return Node(root_value, delete_helper(l, value), r)

# delete root from binary tree
def delete_root(tree: BinTree) -> BinTree:
    if tree == None:
        return None
    else:
        root_value = tree.value
        l = tree.left
        r = tree.right
        
        if l == None:
            return r
        else:
            left_max: int = highest_value( l )
            new_left_subtree: BinTree = delete_highest_value( l )
            return Node( left_max, new_left_subtree, r )

# return the highest value in binary tree
def highest_value( tree : BinTree ) -> int:
    if tree == None:
        raise ValueError( "Called on empty bst." )
    else:
        root_value = tree.value
        l = tree.left
        r = tree.right
        
        if r is None:
            return root_value
        else:
            return highest_value( r )

# delete highest value in binary tree
def delete_highest_value( tree : BinTree ) -> BinTree:
    if tree == None:
        raise ValueError( "Called on empty bst." )
    else:
        root_value = tree.value
        l = tree.left
        r = tree.right
            
        if r is None:
            return l
        else:
            return Node( root_value, l, delete_highest_value( r ) )
