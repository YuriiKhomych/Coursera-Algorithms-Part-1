# Quicksort: O(n log(n))

import random
import time


def qsinplace(a, l, r):
    if l >= r:
        return
    pivot_idx = l
    old_r = r
    pivot = a[l]
    l += 1
    while True:
        # manual check, does it work when l=pivot_idx, r=l+1 for a[l] <= a[r], and for a[l] > a[r] ?
        while a[r] > pivot:
            r -= 1

        if l >= r:
            break

        while l < r and a[l] <= pivot:
            l += 1

        # pre-conditions to swap: l == r, or a[l] > pivot from 2nd loop, and a[r] <= pivot from 1st loop
        a[l], a[r] = a[r], a[l]

    a[pivot_idx], a[r] = a[r], a[pivot_idx]

    qsinplace(a, pivot_idx, r)
    qsinplace(a, r + 1, old_r)


# driver test
l = [i for i in range(0, 100000)]


t1 = time.time()
random.shuffle(l)
t2 = time.time()
print("took ", t2 - t1, " time to shuffle ", len(l))
print(l)
ll = len(l)
t1 = time.time()

# quick sort
qsinplace(l, 0, ll - 1)

t2 = time.time()
print("took ", t2 - t1, " time to qsinplace", len(l))
