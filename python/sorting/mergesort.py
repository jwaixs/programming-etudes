#!/usr/bin/env python

def merge_sort(l):
    '''Merge sort implementation.'''
     
    if type(l) != list:
        raise TypeError, 'Expected list.'

    if len(l) <= 1:
        return l

    middle = len(l)/2
    left = merge_sort(l[:middle])
    right = merge_sort(l[middle:])
 
    ret = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1

    ret += left[i:] + right[j:]

    return ret
