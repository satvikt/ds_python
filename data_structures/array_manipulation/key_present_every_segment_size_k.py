# Python 3 program to find 
# the every segment size of 
# array have a search key x
#
# arr=[21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25]
# x=23
# k=5
# for i in range(0,len(arr),k):
#     # print(i)
#
#     if x not in arr[i:k+i]:
#         print("No")
#         break
#     else:
#         if (i+k) >= len(arr):
#             print("Yes")



# Driver Code
def findxinkindowSize(arr, x, k, n):
    for i in range(0,len(arr),k):
    # print(i)

        if x not in arr[i:k+i]:
            print("No")
            break
        else:
            if (i+k) >= len(arr):
                print("Yes")



if __name__ == "__main__" :

    arr = [ 3, 5, 2, 4, 9, 3,
            1, 7, 3, 11, 12, 3 , 5, 4, 3]
    x, k = 3, 3
    n = len(arr)
    findxinkindowSize(arr, x, k, n)
    # if (findxinkindowSize(arr, x, k, n)) :
    #     print("Yes")
    # else :
    #     print("No")

# This code is contributed 
# by ANKITRAI1
