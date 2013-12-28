def insertion_sort(l):
    if type(l) != list:
        raise TypeError, 'Expect list.'

    if len(l) == 0 or len(l) == 1:
        return l

    for i in range(len(l)):
        j = 0
        while j <= i and l[j] < l[i]:
            j += 1
        l = l[0:j] + [l[i]] + l[j:i] + l[i+1:]

    return l
