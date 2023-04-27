def insert(arr, temp):
    # TODO - will give wrong if [5,2,0] and temp = 1
    # Why are we assuming that arr is sorted here
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return

    val = arr[-1]
    arr.pop()

    insert(arr, temp)
    arr.append(val)
    return


def sort(arr):
    if len(arr) == 1:
        return

    temp = arr[-1]

    arr.pop()
    sort(arr)

    insert(arr, temp)

    return arr

if __name__  == "__main__":
    # arr = [2, 5, 0, 1]
    arr = [5,2,0,1]

    # print(sort(arr))
    sort(arr)

    print(arr)