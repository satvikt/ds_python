def insert(arr, temp):
    """

    :param arr: sorted array
    :param temp: element to be inserted in arr
    :return:
    """
    # if arr is empty, or the element to be inserted is equal or greater than the largest arr element
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return
    val = arr[-1]
    arr.pop()

    # since the base condition wasn't satisfied, insert temp in the shortened array
    insert(arr, temp)

    # append the excluded element in the new arr containing n-2 + temp element
    arr.append(val)
    return


def sort(arr):
    """

    :param arr: given array to be sorted
    :return:
    """
    if len(arr) in (0, 1):
        return
    temp = arr[-1]
    arr.pop()

    sort(arr)
    insert(arr, temp)
    return arr






if __name__  == "__main__":
    # arr = [2, 5, 0, 1]
    # arr = [2, -5,0,1]
    arr = [5,2,0,2,1]

    # print(sort(arr))
    sort(arr)

    print(arr)