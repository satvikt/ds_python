def partition(arr, start, end):
    i, j = 0, 0
    mid = start + (end - start)//2

    arr[end], arr[mid] = arr[mid], arr[end]

    pivot = arr[end]
    i = start

    for j in range(start, end):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[end], arr[i] = arr[i], arr[end]

    return i


def kth_smallest_element(arr, start, end, k):
    if k > len(arr):
        return
    elif k - 1 <= end - start:
        pivot = partition(arr, start, end)

        if pivot == start + k-1:
            return arr[pivot]
        elif pivot > start + k-1:
            return kth_smallest_element(arr, start, pivot - 1, k)
        else:
            return kth_smallest_element(arr, pivot +1, end, k - 1 - (pivot - start))


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]

    k = 4
    print(kth_smallest_element(arr, 0, len(arr)-1, k))