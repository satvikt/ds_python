def findLongestConseqSubseq(arr, n):
    hash_table = set()
    ans = 0
    # count = 0
    # j =0
    for ele in arr:
        hash_table.add(ele)
    for i in range(0, n):
        if arr[i]-1 not in hash_table:
            j = arr[i]
            while j in hash_table:
                j += 1
            ans = max(ans, j-arr[i])
    return ans


if __name__ == "__main__":
    n = 7
    arr = [1, 9, 3, 10, 4, 20, 2]
    print("Length of the Longest contiguous subsequence is ", findLongestConseqSubseq(arr, n))