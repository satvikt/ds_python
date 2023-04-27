# Python program to find maximum contiguous subarray

def maxSubArraySum(a,size):

    max_so_far =a[0]
    curr_max = a[0]

    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)

    return max_so_far

# Driver function to check the above function
a = [5, 4, -2, 6,-1]
b = [7, 1, -8, 4, 9]
print("Maximum contiguous sum is" , maxSubArraySum(b,len(b)))

#This code is contributed by _Devesh Agrawal_
