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

    return t[n][sum]


def can_partition(num):

    total = sum(num)

    if total%2 !=0 :
        return False
    return subset_sum(num,total)

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
