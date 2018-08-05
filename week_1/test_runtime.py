from timeit import timeit

import quick_find_eager
import quick_union_lazy
import weighted_quick_union
import weighted_quick_union_path_compression
from test_quickfind_algoritm import test_quickfind


# Test run time for 10 numbers
for number in [10, 100, 1000, 10000, 100000, 1000000]:
    print(f'!!!Algorithms runtime for {number} numbers!!!')
    time_quick_find_eager = timeit(
        stmt="test_quickfind(quick_find_eager.QuickFindEager)",
        setup="from __main__ import quick_find_eager; from __main__ import test_quickfind",
        number=number
    )
    print(f'Quick Find Eager time {time_quick_find_eager}')
    time_quick_union_lazy = timeit(
        stmt="test_quickfind(quick_union_lazy.QuickUnionLazy)",
        setup="from __main__ import quick_union_lazy; from __main__ import test_quickfind",
        number=number
    )
    print(f'Quick Union Lazy {time_quick_union_lazy}')
    time_weighted_quick_union = timeit(
        stmt="test_quickfind(weighted_quick_union.WeightedQuickUnion)",
        setup="from __main__ import weighted_quick_union; from __main__ import test_quickfind",
        number=number
    )
    print(f'Weighted Quick Union {time_weighted_quick_union}')
    time_weighted_quick_union_path_compression = timeit(
        stmt="test_quickfind(weighted_quick_union_path_compression.WeightedQuickUnionPathCompression)",
        setup="from __main__ import weighted_quick_union_path_compression; from __main__ import test_quickfind",
        number=number
    )
    print(
        'Weighted Quick Union with Path Compression '
        f'{time_weighted_quick_union_path_compression}'
    )