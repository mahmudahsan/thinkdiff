def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert binary_search(arr1, 10) == -1
    assert binary_search(arr1, 5) == 4
    assert binary_search(arr1, 1) == 0
