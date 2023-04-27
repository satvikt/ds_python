# def findxinkindowSize(arr, x, k, n):
#     i = 0
#     j = 0
#     while i < n:
#         while j < k:
#             if i + j < n and arr[i + j] == x:
#                 break
#             j += 1
#         if j == k:
#             return False
#         j = 0
#         i += k
#     if i == n:
#         return True
    # else:/
    #     while

def findxinkindowSize(arr, x, k, n):
    for i in range(0,n,k):
        # if (n%k == 0):
        if x not in arr[i:k+i]:
            return False


if __name__ == "__main__" :

    arr = [ 3, 5, 2, 4, 9, 3,
            1, 7, 3, 11, 12, 3, 5, 4]
    x, k = 3, 3
    n = len(arr)

    if (findxinkindowSize(arr, x, k, n)) :
        print("Yes")
    else :
        print("No")