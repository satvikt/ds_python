def can_partition(arr):
    s = sum(arr)
    n = len(arr)

    t = [[False for x in range(int(s/2)+1)] for y in range(n)]

    for i in range(0, n):
        t[i][0] = True

    for j in range(0, int(s/2)+1):
        t[0][j] = arr[0] == j

    for i in range(1, n):
        for j in range(1, int(s/2)+1):
            if t[i-1][j]:
                t[i][j] = t[i-1][j]
            elif j >= arr[i]:
                t[i][j] = t[i-1][j-arr[i]]

    s1 = 0

    for i in range(int(s/2), -1 ,-1):
        if t[n-1][i]:
            s1 = i
            break

    s2 = s - s1

    return abs(s2 -s1)

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partitxx`ion: " + str(can_partition([1, 3, 100, 4])))


main()