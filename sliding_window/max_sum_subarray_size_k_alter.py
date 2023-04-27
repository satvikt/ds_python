import math


def max_sub_array_of_size_k(k, arr):
    i, j = 0, 0
    win_sum = 0
    max_sum = -math.inf

    while j < len(arr):
        win_sum += arr[j]

        if j-i+1 < k:
            while j-i+1 < k:
                j += 1
                win_sum += arr[j]

        if j-i+1 == k:
            max_sum = max(max_sum, win_sum)
            win_sum -= arr[i]

        i += 1
        j += 1

    return max_sum
def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()