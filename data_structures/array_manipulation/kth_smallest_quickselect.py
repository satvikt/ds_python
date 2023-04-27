def partition(arr, start, end):

    pivot_index = start + (end-start)//2

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    pivot = arr[end]
    j = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    arr[j], arr[end] = arr[end], arr[j]

    return j


def kth_smallest_element(arr, start, end, k):
    if k > len(arr):
        return
    if  k - 1 <= end - start:
        pi = partition(arr, start, end)

        if pi == start + k-1:
            return arr[pi]

        elif pi > start + k-1:
            return kth_smallest_element(arr, start, pi-1, k)

        else:
            return kth_smallest_element(arr, pi+1, end, k -1 - (pi-start))


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]

    k = 4
    print(kth_smallest_element(arr, 0, len(arr)-1, k))