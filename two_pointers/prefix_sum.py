from typing import List
def subarray_sum(arr: List[int], target: int) -> List[int]:
    prefix_sums = {0: -1} # prefix_sum 0 happens when we have an empty array
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        compliment = cur_sum - target
        if compliment in prefix_sums:
            return [prefix_sums[compliment] + 1, i]
        prefix_sums[cur_sum] = i

#Driver code

inputs = ["1 3 -3 8 5 7","1 1 1","1 -20 -3 30 5 7"]
inputs1 = ["5","3","7"]
for i in range(len(inputs)):
    arr = [int(x) for x in inputs[i].split()]
    target = int(inputs1[i])
    res = subarray_sum(arr, target)
    print("Subarray sum :",' '.join(str(e) for e in res))