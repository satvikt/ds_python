def max_sub_array_of_size_k(size, arr):
    i, j = 0, 0
    window_sum, max_sum = 0, 0

    # no point in moving/comparing i, it will only move when we need to `slide` the window to the next set of `size`
    # elements, at line 14
    while j < len(arr):
        # need to calculate things before, lest we should miss current value of i/j
        window_sum += arr[j]
        if j-i+1 < size:
            j += 1
        # Note how if/elif makes the diff - max_sum_subarray_size_k_my.py

        # an if like at max_sum_subarray_size_k_my  will miss out on adding the arr[j] element to window
        # sum (at start of while loop on line 9) before checking the subarray length
        if j-i+1 == size:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i]

            i += 1
            j += 1

    return max_sum


def main():
    print("Maximum sum of a subarray of size 3: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size 2: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

if __name__ == '__main__':
    main()