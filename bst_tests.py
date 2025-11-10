import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**6)
from bst import *

bst_1: BinarySearchTree = BinarySearchTree(comes_before, None)

bst_2: BinarySearchTree = BinarySearchTree(comes_before, Node(1, None, Node(5, None, None)))
bst_3: BinarySearchTree = BinarySearchTree(comes_before, Node(4, None, Node(6, Node(5, None, None), None)))

bst_4: BinarySearchTree = BinarySearchTree(comes_before, Node("thing", None, Node("zebra", None, None)))
bst_5: BinarySearchTree = BinarySearchTree(comes_before, Node("aardvark", None, Node("xylophone", Node("apple", None, None), None)))

bst_6: BinarySearchTree = BinarySearchTree(comes_before, Node(Point2(1, 2), None, Node(Point2(4, 6), None, None)))
bst_7: BinarySearchTree = BinarySearchTree(comes_before, Node(Point2(3, 2), None, Node(Point2(10, 12), Node(Point2(6, 7), None, None), None)))

class BSTTests(unittest.TestCase):
    def test_is_empty(self):
        self.assertEqual(is_empty(bst_1), True)
        self.assertEqual(is_empty(bst_2), False)
        self.assertEqual(is_empty(bst_6), False)
    
    def test_insert(self):
        self.assertEqual(insert(bst_1, Point2(0, 1)), BinarySearchTree(comes_before, Node(Point2(0, 1), None, None)))
        self.assertEqual(insert(bst_2, 0), BinarySearchTree(comes_before, Node(1, Node(0, None, None), Node(5, None, None))))
        self.assertEqual(insert(bst_4, "ants"), BinarySearchTree(comes_before, Node("thing", Node("ants", None, None), Node("zebra", None, None))))
    
    def test_lookup(self):
        self.assertEqual(lookup(bst_1, "anjskdwexsajknewldknqs"), False)
        self.assertEqual(lookup(bst_3, 5), True)
        self.assertEqual(lookup(bst_5, "xylophone"), True)
    
    def test_delete(self):
        self.assertEqual(delete(bst_3, 5), BinarySearchTree(comes_before, Node(4, None, Node(6, None, None))))
        self.assertEqual(delete(bst_3, 4), BinarySearchTree(comes_before, Node(6, Node(5, None, None), None)))
        self.assertEqual(delete(bst_5, "apple"), BinarySearchTree(comes_before, Node("aardvark", None, Node("xylophone", None, None))))

if __name__ == "__main__":
    unittest.main()
