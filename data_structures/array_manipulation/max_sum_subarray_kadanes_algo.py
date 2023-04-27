def kadanes_algo(arr):
    max_so_far = 0
    max_ending_here = 0

    for i in arr:
        max_ending_here = max_ending_here + i

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


if __name__ == "__main__":
    arr = [5, 4, -2, 6,-1]
    print(kadanes_algo(arr))
