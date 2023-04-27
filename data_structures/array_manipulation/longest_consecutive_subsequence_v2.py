def findLongestConseqSubseq(arr, n):
    hash_table = set()
    count = 0
    subseq = []
    result = []
    for ele in arr:
        hash_table.add(ele)

    for i in range(n):
        if arr[i] - 1 not in hash_table:
            #its the beginning of a new subsequence
            subseq = []
            j = arr[i]
            while j in hash_table:
                subseq.append(j)
                j += 1

            if j-arr[i] > count:
                count = max(count, j-arr[i])
                result.append([subseq, count])
    return result



if __name__ == "__main__":
    n = 7
    arr = [1, 9, 3, 10, 4, 20, 2]
    print("Length of the Longest contiguous subsequence is ")
    print(findLongestConseqSubseq(arr, n))
