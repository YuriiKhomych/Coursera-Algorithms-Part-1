# Mergesort: O(n log(n))
from heapq import merge


def mergesort(w):
    """Sort list w and return it."""
    if len(w) < 2:
        return w
    else:
        # sort the two halves of list w recursively with mergesort and merge them
        return merge(mergesort(w[:len(w) // 2]), mergesort(w[len(w) // 2:]))
