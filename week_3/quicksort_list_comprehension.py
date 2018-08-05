# Quicksort: O(n log(n))


def qsort(L):
    if not L: return []
    return qsort([x for x in L[1:] if x < L[0]]) + L[0:1] + \
           qsort([x for x in L[1:] if x >= L[0]])
