def subset_sum_rec(arr, sum, n):
    if sum ==0:
        return True
    if n==0:
        return False

    if arr[n-1] <= sum:
        chosen = subset_sum_rec(arr, sum - arr[n-1], n-1)
        not_chosen = subset_sum_rec(arr, sum, n-1)
        return chosen or not_chosen
    else:
        return subset_sum_rec(arr, sum, n-1)



def subset_sum(arr, sum):
    size = len(arr)
    return subset_sum_rec(arr, sum, size)




if __name__ == "__main__":
    print(subset_sum([1, 2, 3, 5], 7))