def partition_arr(arr, start, end):
    # considering middle element as pivot
    # start = 0
    # end = len(arr) - 1
    # if end == start:
    #     return end
    pivot_index = start + (end-start)//2

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    pivot = arr[end]
    # i = 0
    j = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    arr[end], arr[j] = arr[j], arr[end]

    return j



def quick_sort(arr, start, end):
    if start < end:
        pivot = partition_arr(arr, start, end)

        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot +1, end)


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)