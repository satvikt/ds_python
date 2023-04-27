def subarray_sum(arr, target):
    if len(arr) == 0:
        return
    prefix_sum = {0:-1}
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        compliment = curr_sum - target
        if compliment in prefix_sum:
            return [prefix_sum[compliment] + 1, i]
        prefix_sum[curr_sum] = i


if __name__ == '__main__':
    inputs = ["1 3 -3 8 5 7","1 1 1","1 -20 -3 30 5 7"]
    inputs1 = ["5","3","7"]
    for i in range(len(inputs)):
        arr = [int(x) for x in inputs[i].split()]
        target = int(inputs1[i])
        res = subarray_sum(arr, target)
        print("Subarray sum :",' '.join(str(e) for e in res))