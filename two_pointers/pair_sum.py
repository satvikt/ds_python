def pair_sum(arr, sum):
    dic = {}
    lis = []

    for i in arr:
        if (sum - i) in dic:
            lis.append((i, sum - i))
        else:
            dic[i] = sum - i

    return lis if lis else "No pair found"

"""
The below takes care of 
1. when there are duplicates in arr (that when paired with another num) total up to sum.
However, it assumes that "reusing" a number in more than 1 pair`, is allowed. 
"""
def pair_sum_alter(arr, sum):
    # dic = {}
    lis = [0]*20

    for i in arr:
        lis[i] += 1

    twice_count = 0

    for i in range(len(arr)):
        twice_count += lis[sum - arr[i]]

        if sum - arr[i] == arr[i]:
            twice_count -= 1

    return int(twice_count/2)





if __name__ == '__main__':
    A = [6, 5, 5, 4, 3]

    K = 9

    # print(pair_sum(A, K))
    print(pair_sum_alter(A, K))