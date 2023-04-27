# Driver Code 
def UnionArray(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    out_table = {}

    # for ele in arr1:
    #     if ele in out_table:
    #         out_table[ele] += 1
    #     else:
    #         out_table[ele] = 1
    out_table[arr1[0]] = 1
    for i in range(1, m):
        if arr1[i] != arr1[i-1]:
            out_table[arr1[i]] = 1

    print(out_table)

    # for j in range(n):
    for j in range(n):
        if arr2[j] not in out_table:
            out_table[arr2[j]] = 1

    for key in out_table.keys():
        print(key, end=" ")


if __name__ == "__main__":

    arr1 = [1, 2, 2, 2, 3]
    arr2 = [2, 3, 4, 5]

    # print(UnionArray(arr1, arr2))
    UnionArray(arr1, arr2)