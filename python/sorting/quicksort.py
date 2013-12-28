#!/usr/bin/env python

def quick_sort(l):
    '''Quicksort implementation.'''

    if type(l) != list:
        raise TypeError, 'Expected list.'

    if len(l) == 0 or len(l) == 1:
        return l
    else:
        pivot = l[0]
        return quick_sort([elm for elm in l if elm < pivot]) \
            + [elm for elm in l if elm == pivot] \
            + quick_sort([elm for elm in l if elm > pivot])
