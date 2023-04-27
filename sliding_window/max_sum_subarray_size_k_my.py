import math


def max_sub_array_of_size_k(k, arr):
    sum, win_sum = 0, 0
    i, j = 0,0

    while j < len(arr):
        win_sum = win_sum + arr[j]

        if j-i+1 < k:
            j += 1
        if j-i+1 == k:
            sum = max(sum, win_sum)

            win_sum -= arr[i]

            j += 1
            i += 1

    return sum

def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()