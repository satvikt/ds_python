def insert(arr, temp):
    if len(arr) == 0 or temp > arr[-1]:
        arr.append(temp)
        return

    val = arr[-1]

    arr.pop()
    insert(arr,temp)

    arr.append(val)

    return arr


def sort(arr):
    if len(arr) in [0, 1]:
        return

    temp = arr[-1]

    arr.pop()
    sort(arr)

    insert(arr, temp)
    return arr

if __name__  == "__main__":
    # arr = [2, 5, 0, 1]
    arr = [2, -5,0,1]

    # print(sort(arr))
    sort(arr)

    print(arr)