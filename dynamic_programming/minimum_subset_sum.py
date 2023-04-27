from math import ceil

def subset_sum(arr, sum):
    n = len(arr)
    t = [[False for j in range(sum+1)] for i in range(n+1)]

    for j in range(sum+1):
        t[0][j] = False

    for i in range(n+1):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                chosen = t[i-1][j-arr[i-1]]
                not_chosen = t[i-1][j]

                t[i][j] = chosen or not_chosen

            else:
                t[i][j] = t[i-1][j]

    return t[n]

def can_partition(arr):
    # subset_sum (arr, sum)
    # create a matrix of t[n+1][(sum+1)//2)
    # return the index of  rightmost "True" column of the final row t[n]
        # that will be the largest value possible for s1

    total = sum(arr)

    half = total//2

    last_row = subset_sum(arr, half)

    s1 = 0

    for i in range(half,-1,-1):
        if last_row[i] == True:
            s1 = i
            break

    return total - 2*s1

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()