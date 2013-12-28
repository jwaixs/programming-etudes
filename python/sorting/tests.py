import random
import unittest

from selectsort import selection_sort
from insertsort import insertion_sort
from quicksort import quick_sort
from mergesort import merge_sort
from heapsort import heapsort

class TestSortingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.N = 100
        self.seq = range(self.N)
    
    def test_selection_sort(self):
        self.assertRaises(TypeError, selection_sort, (1, 2, 3))
        self.assertRaises(TypeError, selection_sort, 1)
        self.assertRaises(TypeError, selection_sort, 'helloworld!')
 
        random.shuffle(self.seq)
        self.seq = selection_sort(self.seq)
        self.assertEqual(self.seq, range(self.N))
    
    def test_insertion_sort(self):
        self.assertRaises(TypeError, insertion_sort, (1, 2, 3))
        self.assertRaises(TypeError, insertion_sort, 1)
        self.assertRaises(TypeError, insertion_sort, 'helloworld!')
 
        random.shuffle(self.seq)
        self.seq = insertion_sort(self.seq)
        self.assertEqual(self.seq, range(self.N))

    def test_quick_sort(self):
        self.assertRaises(TypeError, quick_sort, (1, 2, 3))
        self.assertRaises(TypeError, quick_sort, 1)
        self.assertRaises(TypeError, quick_sort, 'helloworld!')
 
        random.shuffle(self.seq)
        self.seq = quick_sort(self.seq)
        self.assertEqual(self.seq, range(self.N))
    
    def test_merge_sort(self):
        self.assertRaises(TypeError, merge_sort, (1, 2, 3))
        self.assertRaises(TypeError, merge_sort, 1)
        self.assertRaises(TypeError, merge_sort, 'helloworld!')
 
        random.shuffle(self.seq)
        self.seq = merge_sort(self.seq)
        self.assertEqual(self.seq, range(self.N))

    def test_heapsort(self):
        self.assertRaises(TypeError, heapsort, (1, 2, 3))
        self.assertRaises(TypeError, heapsort, 1)
        self.assertRaises(TypeError, heapsort, 'helloworld!')
 
        random.shuffle(self.seq)
        self.seq = heapsort(self.seq)
        self.assertEqual(self.seq, range(self.N))
    

if __name__ == '__main__':
    unittest.main()
