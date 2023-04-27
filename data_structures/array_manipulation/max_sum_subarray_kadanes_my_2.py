def maxSubArraySum(a):
    max_ending_here = 0
    max_so_far = 0
    start = end = 0
    s = 0
    for i in range(len(a)):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1


    print ("Maximum contiguous sum is %d"%(max_so_far))
    print ("Starting Index %d"%(start))
    print ("Ending Index %d"%(end))
    return max_so_far



if __name__ == "__main__":
    # Driver function to check the above function
    # a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    # b = [-2, -3, 4, -1, -2, 1, 5, -3]
    b = [5, 4, -2, 6,-1]
    print("Maximum contiguous sum is", maxSubArraySum(b))