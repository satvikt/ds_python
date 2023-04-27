import random3


def choose_pivot(left, right):
    i1 = left + random3.randint(0, right - left)
    i2 = left + random3.randint(0, right - left)
    i3 = left + random3.randint(0, right - left)

    return max(min(i1, i2), min(max(i1,i2), i3))


def partition(arr, left, right):
    pivot_index = choose_pivot(left, right)

    arr[right], arr[pivot_index] = arr[pivot_index], arr[right]

    pivot = arr[right]
    i = left -1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[right], arr[i+1] = arr[i+1], arr[right]

    return i+1


def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)

        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)



# Driver code to test above
if __name__ == '__main__':

    lst = [5, 4, 2, 1, 3]
    quick_sort(lst, 0, len(lst) - 1)

    # Printing Sorted list
    print("Sorted list: ", lst)