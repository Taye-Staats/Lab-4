import sys 
import unittest 
from typing import * 
from dataclasses import dataclass 
sys.setrecursionlimit(10**6) 
from bst import * 




class BSTTests(unittest.TestCase): 
    # Testing isEmpty
    def test_isEmpty(self): 
        bst : BinarySearchTree = BinarySearchTree(lambda a,b: a<b, None)
        bst2 : BinarySearchTree = BinarySearchTree(lambda a,b: a<b, Node(1, None, None))
        bst3 : BinarySearchTree = BinarySearchTree(lambda a,b: a<b, Node("a", None, None))
        bst4 : BinarySearchTree = BinarySearchTree(lambda a,b: a<b, Node(Point2(0,0), None, None))
        self.assertEqual(isEmpty(bst), True)
        self.assertEqual(isEmpty(bst2), False)
        self.assertEqual(isEmpty(bst3), False)
        self.assertEqual(isEmpty(bst4), False)
    # Testing insert
    def test_insert(self):
        cmp = lambda a, b: a < b
        bst : BinarySearchTree = BinarySearchTree(cmp, Node(1, None, None))
        bst2 : BinarySearchTree = BinarySearchTree(cmp, Node("a", None, None))
        bst4 : BinarySearchTree = BinarySearchTree(cmp, Node(Point2(0,0), None, None))
        bstA : BinarySearchTree = BinarySearchTree(cmp, Node(bst.tree.value, None, Node(2, None, None)))
        bstA2 : BinarySearchTree = BinarySearchTree(cmp,  Node(bst.tree.value, Node(0, None, None), None))
        bstA3  : BinarySearchTree = BinarySearchTree(cmp, Node(bst2.tree.value, None, Node("b", None, None)))
        bstA4 : BinarySearchTree = BinarySearchTree(cmp, Node(Point2(0,0), None, Node(Point2(1,1), None, None)))
        self.assertEqual(insert(bst, 2), bstA)
        self.assertEqual(insert(bst, 0), bstA2)
        self.assertEqual(insert(bst2, "b"), bstA3)
        self.assertEqual(insert(bst4, Point2(1,1)), bstA4)
    # Testing lookup
    def test_lookup(self):

        bst : BinarySearchTree = BinarySearchTree(lambda a,b: a<b, Node(1, None, None)) 
        bst2 : BinarySearchTree = BinarySearchTree(lambda a,b: a<b, Node(0, None, None)) 
        bst3 : BinarySearchTree = BinarySearchTree(lambda a,b: a<b, Node(0, Node(1, None, None), Node(2, None, None))) 
        bst4 : BinarySearchTree = BinarySearchTree(lambda a,b: a<b, Node(5, Node(2, Node(1, None, None), None), Node(10, None, None)))
        bst5 : BinarySearchTree = BinarySearchTree(lambda a,b: a<b, Node("a", None, None)) 
        bst6 : BinarySearchTree = BinarySearchTree(lambda a,b: a<b, Node("a", None, Node("b", None, None))) 
        self.assertEqual(lookup(bst, 1), True)
        self.assertEqual(lookup(bst2, 2), False)
        self.assertEqual(lookup(bst3, 3), False)
        self.assertEqual(lookup(bst4, 7), False)
        self.assertEqual(lookup(bst4, 10), True)
        self.assertEqual(lookup(bst4, 3), False)
        self.assertEqual(lookup(bst5, "a"), True)
        self.assertEqual(lookup(bst5, "b"), False)
        self.assertEqual(lookup(bst6, "b"), True)
if (__name__ == '__main__'): 
    unittest.main()