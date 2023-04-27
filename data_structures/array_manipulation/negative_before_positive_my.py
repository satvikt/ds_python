def negative_before_positive(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        while arr[start] < 0:# and start <=end:
            start += 1
        while arr[end] > 0:# and start <=end:
            end -= 1
        # if start <=end and arr[start] >0 :
        if arr[start] >0 :
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    return arr

if __name__ == "__main__":
    arr = [-1,-1, -2, -5, -2,-6]
    arr0 = [1,2,3]
    # print(arr0)
    arr1 = [1,2,3,-1,-2]#
    # print(negative_before_positive(arr0))
    print(negative_before_positive(arr1))
    # print(arr0)
