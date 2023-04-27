def swap(arr):
    length = len(arr)
    if length == 1:
        return arr
    if length % 2 != 0:
        length -= 1
    for i in range(0, length, 2):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
    return arr

if __name__ == "__main__" :
    arr = "satvik"
    print("original {}".format(arr))
    print("".join(swap(list(arr))))
