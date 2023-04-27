import copy


def combination_rec(start, curr_sum, sum, local, arr, final):
    if curr_sum == sum:
        final.append(copy.copy(local))

    for i in range(start, len(arr)):
        if curr_sum + arr[i] > sum: #no need to check for rest of the elements
            break

        if i > start and arr[i] == arr[i-1]: #if we encountered a duplicate element
            continue

        local.append(arr[i])

        combination_rec(i+1, curr_sum+arr[i], sum, local, arr, final)

        local.remove(arr[i])


def combination(arr, sum):
    arr.sort(reverse=False)
    local = []
    final = []
    combination_rec(0, 0, sum, local, arr, final)
    if final:
        return final
    return []


if __name__ == "__main__":
    arr = [1,2,3]
    sum = 3
    
    print(combination(arr, sum))