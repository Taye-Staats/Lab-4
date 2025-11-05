import sys 
import unittest 
from typing import * 
from dataclasses import dataclass 
import math
sys.setrecursionlimit(10**6)

# Data defention for BinTree
BinTree : TypeAlias = Union['Node', None]

# Data defention for Node
@dataclass(frozen=True)
class Node:
    value : Any
    left : BinTree
    right : BinTree

# Data defention for BinarySearchTree
@dataclass(frozen=True)
class BinarySearchTree:
    comes_before : Callable[[Any,Any],bool] 
    tree : BinTree
@dataclass(frozen=True)
class Point2:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
# A function that returns true if binary search tree is empty and false otherwise
def isEmpty(bst : BinarySearchTree) -> bool:
    if bst.tree is None:
        return True
    return False

# Add a value to the tree, if the value comes before put it in the left, if it doesn't put it in right
def insert(bst : BinarySearchTree, val : Any) -> BinarySearchTree:
    return BinarySearchTree(bst.comes_before, insert_helper(bst, val))
# Insert helper that handles making the new tree
def insert_helper(bst : BinarySearchTree, val : Any) -> BinTree:
    match bst.tree:
        case None:
            return  Node(val, None, None)
        case Node(root, left, right):
            if root == val:
                return bst.tree
            elif comes_before(val, root):
                return Node(root, insert_helper(BinarySearchTree(bst.comes_before, left), val),right)
            else:
                return Node(root, left, insert_helper(BinarySearchTree(bst.comes_before, right), val))

# comes_before function that works for both Point2 and other types
def comes_before(x : Any, y : Any) -> bool:
    if isinstance(x, Point2) and isinstance(y, Point2):
        return x.distance_from_origin() < y.distance_from_origin()
    else:
        return x < y
# Finds if a value is in a BinarySearchTree by seeing if both values don't come before the other
def lookup(bst : BinarySearchTree, val : Any) -> bool:
    if bst.tree is None:
        return False
    if not comes_before(val, bst.tree.value) and not comes_before(bst.tree.value, val):
        return True
    if comes_before(val, bst.tree.value):
        return lookup(BinarySearchTree(bst.comes_before, bst.tree.left), val)
    else:
        return lookup(BinarySearchTree(bst.comes_before, bst.tree.right), val)

# If value exists in the tree remove it and preserve the BST properties
def delete(bst : BinarySearchTree, val : Any) -> BinarySearchTree:
    match bst.tree:
        case None:
            return bst
        case Node(root, left, right):
            if root == val:
                return BinarySearchTree(bst.comes_before, delete_root(bst))
            elif comes_before(val, root):
                return delete(BinarySearchTree(bst.comes_before, left), val)
            else:
                return delete(BinarySearchTree(bst.comes_before, right),val)
# Deletes the root
def delete_root(bst : BinarySearchTree) -> BinTree:
    match bst.tree:
        case None:
            return None
        case Node(root, left, right):
            if left is None:
                return right
            else:
                left_max : int = highest_value( left )
                new_left_subtree : Node = delete_highest_value(left)
                return Node(left_max, new_left_subtree, right)
# Returns the highest value in a tree
def highest_value(bst : BinTree) -> int:
    match bst:
        case None:
            raise ValueError( "Called on empty bst." )
        case Node(root, left, right):
            if right is None:
                return root
            else:
                return highest_value(right)
# Deletes the hgihest value in a tree
def delete_highest_value(bst : BinTree) -> BinTree:
    match bst:
        case None:
            raise ValueError( "Called on empty bst." )
        case Node(root, left, right):
            if right is None:
                return left
            else:
                return delete_highest_value(root, left, delete_highest_value(right))