def max_subarray_sum(arr, start, end):
    if len(arr) > 0:
        mid = start + (end - start)//2




if __name__ == "__main__":
    arr = [7, 1, -8, 4, 9]
    print(max_subarray_sum(arr, 0, len(arr)))