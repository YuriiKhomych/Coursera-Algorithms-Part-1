# Mergesort: O(n log(n))

def merge(lst, frm, pivot, to, len1, len2):
    if len1 == 0 or len2 == 0: return
    if len1 + len2 == 2:
        if lst([pivot]) < lst[frm]: lst[pivot], lst[frm] = lst[frm], lst[pivot]
        return
    if len1 > len2:
        len11 = len1 / 2
        firstcut, secondcut, length = frm + len11, pivot, to - pivot
        while length > 0:
            half = length / 2
            mid = secondcut + half
            if lst[mid] < lst[firstcut]:
                secondcut, length = mid + 1, length - half - 1
            else:
                length = half
        len22 = secondcut - pivot
    else:
        len22 = len2 / 2
        firstcut, secondcut, length = frm, pivot + len22, pivot - frm
        while length > 0:
            half = length / 2
            mid = firstcut + half
            if lst[secondcut] < lst[mid]:
                length = half
            else:
                firstcut, length = mid + 1, length - half - 1
        len11 = firstcut - frm
    if firstcut != pivot and pivot != secondcut:
        n, m = secondcut - firstcut, pivot - firstcut
        while m != 0: n, m = m, n % m
        while n != 0:
            n -= 1
            p1, p2 = firstcut + n, n + pivot
            val, shift = lst[p1], p2 - p1
            while p2 != firstcut + n:
                lst[p1], p1 = lst[p2], p2
                if secondcut - p2 > shift:
                    p2 += shift
                else:
                    p2 = pivot - secondcut + p2
            lst[p1] = val
    newmid = firstcut + len22
    merge(lst, frm, firstcut, newmid, len11, len22)
    merge(lst, newmid, secondcut, to, len1 - len11, len2 - len22)


def sort(lst, frm=0, to=None):
    if to is None: to = len(lst)
    if to - frm < 2: return
    middle = (frm + to) / 2
    sort(lst, frm, middle)
    sort(lst, middle, to)
    merge(lst, frm, middle, to, middle - frm, to - middle)
