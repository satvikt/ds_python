def right_rotate(arr, length, out_of_place, i):
    temp = arr[i]
    for j in range(i, out_of_place, -1):
        arr[j] = arr[j-1]
    arr[out_of_place] = temp


def rearrange(arr, length):
    out_of_place = -1

    for i in range(length):
        if out_of_place == -1:
            if (arr[i] >=0 and i%2 ==0) or (arr[i] <0 and i%2 == 1):
                out_of_place = i
        if (arr[i] >=0 and arr[out_of_place] <0) or (arr[i]<0 and arr[out_of_place] >0):
            right_rotate(arr, length, out_of_place, i)
            if i - out_of_place > 2:
                out_of_place += 2
            else:
                out_of_place = -1


if __name__ == "__main__":
    # Driver Code
    arr = [-5, -2, 5, 2, 4,
           7, 1, 8, 0, -8]

    print("Given Array is:")
    print(arr)

    print("\nRearranged array is:")
    print(rearrange(arr, len(arr)))