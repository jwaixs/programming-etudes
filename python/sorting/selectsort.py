def selection_sort(l):
    if type(l) != list:
        raise TypeError, 'Expected list.'

    ret = []

    for i in range(len(l)):
        imin = 0
        for j in range(len(l)):
            if l[j] < l[imin]:
                imin = j
        ret.append(l[imin])
        l.remove(l[imin])

    return ret
