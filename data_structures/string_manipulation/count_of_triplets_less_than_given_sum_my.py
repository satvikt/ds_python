def countTriplets(arr, n, sum):
    arr.sort()
    total = 0
    for i in range(n-2):
        j = i+1
        k = n-1
        while j < k:
            if arr[i] + arr[j] + arr[k] >= sum:
                k -= 1
            else:
                possible = k-j
                # if possible > 0:
                #     total += possible
                #     j +=
                # else:
                #     break
                total += possible
                j += 1
    return total
#
if __name__ == "__main__":
    arr = [5, 1, 3, 4, 7]
    n = len(arr)
    sum = 12
    print(countTriplets(arr, n, sum))

