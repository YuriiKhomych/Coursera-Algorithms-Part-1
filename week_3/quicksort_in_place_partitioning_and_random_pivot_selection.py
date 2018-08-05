# Quicksort: O(n log(n))


import random


def _doquicksort(values, left, right):
    """Quick sort"""

    def partition(values, left, right, pivotidx):
        """In place partitioning from left to right using the element at
        pivotidx as the pivot. Returns the new pivot position."""

        pivot = values[pivotidx]
        # swap pivot and the last element
        values[right], values[pivotidx] = values[pivotidx], values[right]

        storeidx = left
        for idx in range(left, right):
            if values[idx] < pivot:
                values[idx], values[storeidx] = values[storeidx], values[idx]
                storeidx += 1

        # move pivot to the proper place
        values[storeidx], values[right] = values[right], values[storeidx]
        return storeidx

    if right > left:
        # random pivot
        pivotidx = random.randint(left, right)
        pivotidx = partition(values, left, right, pivotidx)
        _doquicksort(values, left, pivotidx)
        _doquicksort(values, pivotidx + 1, right)

    return values


def quicksort(mylist):
    return _doquicksort(mylist, 0, len(mylist) - 1)
