#!/usr/bin/env python

def sink(alist, start, end):
    root = start

    while 2*root + 1 <= end:
        child = 2*root + 1
        swap = root

        if alist[swap] <= alist[child]:
            swap = child
        if child+1 <= end and alist[swap] < alist[child+1]:
            swap = child + 1
        if swap != root:
            alist[root], alist[swap] = alist[swap], alist[root]
            root = swap
        else:
            return

def heapify(alist):
    start = (len(alist) - 2) / 2

    while start >= 0:
        sink(alist, start, len(alist)-1)
        start -= 1

def heapsort(alist):
    '''Heapsort implementation.'''

    if type(alist) != list:
        raise TypeError, 'Expected list.'

    heapify(alist)

    end = len(alist) - 1
    while end > 0:
        alist[end], alist[0] = alist[0], alist[end]
        end -= 1
        sink(alist, 0, end)

    return alist
