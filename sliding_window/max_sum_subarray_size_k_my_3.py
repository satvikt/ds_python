def max_sub_array_of_size_k(size, arr):
    i, j = 0, 0
    window_sum, max_sum = 0, 0

    while i < len(arr):
        if j-i+1 < size:
            window_sum += arr[j]
            max_sum = max(max_sum, window_sum)
            j += 1
        elif j-i+1 == size:
            window_sum += arr[j]
            max_sum = max(max_sum, window_sum)
            j += 1
            i += 1



def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

if __name__ == '__main__':
    main()