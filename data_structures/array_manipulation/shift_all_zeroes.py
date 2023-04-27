def shift_all_zeroes(arr):
    start = 0
    non_zero = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            non_zero += 1



if __name__ == "__main__":
    shift_all_zeroes([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9])