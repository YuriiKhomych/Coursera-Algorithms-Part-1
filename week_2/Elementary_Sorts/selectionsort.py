# Selection Sort: O(n^2)

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def selectionsort(array):
    for i in range(0, len(array)):
        i_smallest = i
        for j in range(i+1, len(array)):
            if array[j] < array[i_smallest]:
                i_smallest = j
        swap(array, i, i_smallest)


if __name__ == "__main__":
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    selectionsort(array)
    print(array)
