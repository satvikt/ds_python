def remove_duplicates(arr):
    i = 1
    next_non_dup = 1

    for i in range(len(arr)):
        if arr[next_non_dup-1] != arr[i]:
            arr[next_non_dup] = arr[i]
            next_non_dup += 1
        i += 1
    return arr[:next_non_dup]


if __name__ == '__main__':
    A = [2, 3, 3, 3, 6, 9, 9]

    print(remove_duplicates(A))