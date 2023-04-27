import copy


def combination_rec(start, curr_sum, sum, arr, local, final):
    if curr_sum == sum:
        final.append(copy.copy(local))

    for i in range(start, len(arr)):
        if curr_sum + arr[i] > sum:
            break
        if i > start and arr[i-1] == arr[i]:
            continue

        local.append(arr[i])

        combination_rec(i+1, curr_sum + arr[i], sum, arr, local, final)

        local.remove(arr[i])


def combination(arr, sum):
    arr.sort()
    local = []
    final = []

    combination_rec(0, 0, sum, arr, local, final)

    return final


if __name__ == "__main__":
    arr = [1,1, 2,3]
    sum = 4
    print(combination(arr, sum))