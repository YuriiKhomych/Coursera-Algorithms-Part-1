import quick_find_eager
import quick_union_lazy
import weighted_quick_union
import weighted_quick_union_path_compression


def test_quickfind(quickfind):
    # print(f'---{quickfind.__name__}---')
    t = quickfind(100)
    t.union(1, 2)
    # print('1) OK!' if True == t.connected(1,2) else "Not OK!")
    t.union(4, 2)
    t.union(3, 4)
    # print('2) OK!' if False == t.connected(0,2) else "Not OK!")
    # print('3) OK!' if True == t.connected(1,4) else "Not OK!")
    t.union(0, 3)
    # print('4) OK!' if True == t.connected(0,4) else "Not OK!")
    t.union(50, 0)
    t.union(34, 8)
    # print('5) OK!' if True == t.connected(8,34) else "Not OK!")
    t.union(48, 5)
    t.union(54, 17)
    t.union(17, 83)
    # print('6) OK!' if False == t.connected(17,1) else "Not OK!")
    t.union(17, 48)
    t.union(9, 6)
    t.union(57, 63)
    # print('7) OK!' if False == t.connected(2,34) else "Not OK!")
    t.union(64, 65)
    t.union(72, 83)
    t.union(63, 83)
    # print('8) OK!' if False == t.connected(6,34) else "Not OK!")
    # print('9) OK!' if False == t.connected(17,1) else "Not OK!")
    # print('===END===')

if __name__ == '__main__':
    # Accuracy Checks
    test_quickfind(quick_find_eager.QuickFindEager)
    test_quickfind(quick_union_lazy.QuickUnionLazy)
    test_quickfind(weighted_quick_union.WeightedQuickUnion)
    test_quickfind(weighted_quick_union_path_compression.WeightedQuickUnionPathCompression)
